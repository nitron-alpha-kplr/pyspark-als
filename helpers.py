from pyspark.sql.types import *
import os

def make(*args, spark=None):
    if not os.path.isdir('ml-latest-small'):
        os.system('wget http://files.grouplens.org/datasets/movielens/ml-latest-small.zip')
        os.system('unzip ml-latest-small.zip')
    result = []
    for arg in args:
        if arg == 'ratings':
            ratings_schema = StructType([
                StructField('user'     , IntegerType()),
                StructField('movie'    , IntegerType()),
                StructField('rating'   , DoubleType() ),
                StructField('timestamp', LongType()   ),
            ])
            ratings = spark.read.csv('ml-latest-small/ratings.csv', header=True, schema=ratings_schema).select(['user' , 'movie', 'rating'])
            result.append(ratings)
        if arg == 'movies':
            movies_schema = StructType([
                StructField('movie' , IntegerType()),
                StructField('title' , StringType ()),
                StructField('genres', StringType ()),
            ])
            movies  = spark.read.csv('ml-latest-small/movies.csv' , header=True, schema=movies_schema ).select(['movie', 'title', 'genres'])
            result.append(movies)
    if len(result) == 1:
        return result[0]
    else:
        return tuple(result)