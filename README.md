# pyspark-als
Alternating Least Squares (ALS) matrix factorization using pyspark


### Params Grid Search
Cool way to do gridsearch is `TrainValidationSplit` and `ParamGridBuilder`  
but it is broken for many models including `ALS`  
it doesn't save all params to `bestModel`  
therefore I use my own grid search implementation

see [modeling - How to extract model hyper-parameters from spark.ml in PySpark? - Stack Overflow](https://stackoverflow.com/questions/36697304/how-to-extract-model-hyper-parameters-from-spark-ml-in-pyspark)


---

По идее нужно делать CV на каждом наборе параметров. Не на одном `random train test split`  а на 3 хотя бы 


---

maxIter - as rule of thumb: if `abs(metric[i]` - `metric[i - 1]) < 0.001` - stop iteration  
Ну bigger is better, точнее матрица разлагается  
[Тут пишут](https://spark.apache.org/docs/latest/mllib-collaborative-filtering.html), что ALS typically converges to a reasonable solution in 20 iterations or less. Хз мне кажется мало, потому что чет не очень в тему предлагает по жанрам)

---
