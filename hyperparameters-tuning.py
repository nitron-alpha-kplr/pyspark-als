# maxIter не надо искать, с ним все понятно: bigger is better


### Params Grid Search
Cool way to do gridsearch is `TrainValidationSplit` and `ParamGridBuilder`  
but it is broken for many models including `ALS`  
it doesn't save all params to `bestModel`  
therefore I use my own grid search implementation

see [modeling - How to extract model hyper-parameters from spark.ml in PySpark? - Stack Overflow](https://stackoverflow.com/questions/36697304/how-to-extract-model-hyper-parameters-from-spark-ml-in-pyspark)


---

По идее нужно делать CV на каждом наборе параметров. Не на одном `random train test split`  а на 3 хотя бы 


---
