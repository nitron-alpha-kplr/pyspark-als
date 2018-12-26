Cool way to do grid search in pyspark is using `TrainValidationSplit`/`CrossValidator` and `ParamGridBuilder`  
but it is broken for many models including `ALS`:  
`bestModel` does not contains needed params, which you specify in ParamGridBuilder and want to optimize. So it's useless

therefore I use my own grid search implementation instead

see [modeling - How to extract model hyper-parameters from spark.ml in PySpark? - Stack Overflow](https://stackoverflow.com/questions/36697304/how-to-extract-model-hyper-parameters-from-spark-ml-in-pyspark)


```py
param_grid = ParamGridBuilder()                \
    .addGrid(als.regParam, [0.17, 0.18, 0.19]) \
    .build()

evaluator = RegressionEvaluator(metricName='rmse', labelCol='rating', predictionCol='prediction')

tvs = TrainValidationSplit(
    estimator = als,
    estimatorParamMaps = param_grid,
    evaluator = evaluator,
)

train, test = ratings.randomSplit([0.8, 0.2])

best_model = tvs.fit(train).bestModel

```
