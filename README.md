# pyspark-als

Alternating Least Squares (ALS) matrix factorization using pyspark

----------------------------------------------------------------

<details>
<summary>explicit ratings vs implicit feedback</summary>

- r is now not rating but feedback data / interaction matrix (number of views, clicks, play count, time spent on a page, etc) - про диапазон значений r есть инфа в [original paper](http://yifanhu.net/PUB/cf.pdf) Раздел Preliminaries
- Короче, по идее ничего не нужно в коде менять. Просто подаешь свою interaction-matrix и добавляешь в `ALS`: 
- `implicitPrefs=True, alpha=1.0`  
- `alpha` - one more hyperparameter to tune. In the paper they found `alpha = 40` to work well and somewhere between `15 and 40 worked for other guy from medium`


https://spark.apache.org/docs/2.3.0/mllib-collaborative-filtering.html#tutorial

if the rating matrix is derived from another source of information (i.e. it is inferred from other signals), you can set implicitPrefs to True to get better results:

пока не до конца понял

[`суть`](https://youtu.be/58OjaDH2FI0?t=509)


grouplens dataset contains explicit ratings  
but my real dataset is implicit feedback data  
so I use implicit here for code consistency  
the only difference is `implicitPrefs=True` and additional `alpha` parameter

также графики тоже стремные, потому что я юзаю implicit, хотя данные explicit. Делаю так потому чтобы code consistency был

в принципе можно просто grouplens dataset отскейлить, но пофиг

</details>

----------------------------------------------------------------

<details>
<summary>gridsearch note</summary>

Cool way to do grid search in pyspark is to use `TrainValidationSplit`/`CrossValidator` and `ParamGridBuilder`  
but it is broken for many models including `ALS`:  
`bestModel` does not contains needed params, which you specify in ParamGridBuilder and want to optimize.   
So it's useless

therefore I use my own grid search implementation instead (btw I use random search instead of grid search)

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
maxIter не надо искать, с ним все понятно: bigger is better (точнее матрица разлагается)
maxIter - as rule of thumb: if `abs(metric[i] - metric[i - 1]) < 0.001` - stop iteration
(ну нет api-доступа к внутренностям)  
[Тут пишут](https://spark.apache.org/docs/latest/mllib-collaborative-filtering.html), что ALS typically converges to a reasonable solution in 20 iterations or less. Хз в принципе можно и больше делать

</details>
