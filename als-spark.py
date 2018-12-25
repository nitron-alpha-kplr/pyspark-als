from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()
# spark.sparkContext.setLogLevel('INFO')


spark.sparkContext.setCheckpointDir('checkpoint/') # https://stackoverflow.com/a/31484461

from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.recommendation import ALS
from pyspark.ml.tuning import TrainValidationSplit, ParamGridBuilder
from pyspark.sql.types import *

from itertools import product
import numpy as np

schema = StructType([
    StructField('user'     , IntegerType()),
    StructField('movie'    , IntegerType()),
    StructField('rating'   , DoubleType() ),
    StructField('timestamp', LongType()   ),
])

ratings = spark.read.csv('ratings.csv', header=True, schema=schema).select(['user', 'movie', 'rating'])
# ratings = ratings.limit(500)
ratings.show()

train, test = ratings.randomSplit([0.8, 0.2])


param_fixed = {
    'userCol'          : 'user', 
    'itemCol'          : 'movie', 
    'ratingCol'        : 'rating', 
    'coldStartStrategy': 'drop', 
    'nonnegative'      : True,
}

param_grid = {
    'rank'    : range(4, 12),
    'maxIter' : range(2, 20, 2),
    'regParam': list(np.linspace(0.001, 0.4, 10)),
}

pgrid = [
    dict(zip(param_grid.keys(), param_comb))
    for param_comb in product(*param_grid.values())
]

# random search instead of grid search
from random import sample
pgrid = sample(pgrid, 100)

def evaluate_params(params, model_class, param_fixed, evaluator, train, test):
    model = model_class(**params, **param_fixed)
    predictions = model.fit(train).transform(test)
    score = evaluator.evaluate(predictions)
    return (params, score)

def evaluate_als(params):
    return evaluate_params(
        params      = params     ,
        model_class = ALS        ,
        param_fixed = param_fixed,
        evaluator   = evaluator  ,
        train       = train      ,
        test        = test       ,
    )

evaluator = RegressionEvaluator(metricName='rmse', labelCol='rating', predictionCol='prediction')

from multiprocessing.dummy import Pool # dummy means threads, not real processes

# pool = Pool(processes=len(pgrid))
pool = Pool(processes=20)
z = pool.map(evaluate_als, pgrid)

for i in sorted(z, key = lambda x: x[1]):
    print(i)
