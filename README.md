# pyspark-als
Alternating Least Squares (ALS) matrix factorization using pyspark


maxIter - as rule of thumb: if `abs(metric[i]` - `metric[i - 1]) < 0.001` - stop iteration  
Ну bigger is better, точнее матрица разлагается  
[Тут пишут](https://spark.apache.org/docs/latest/mllib-collaborative-filtering.html), что ALS typically converges to a reasonable solution in 20 iterations or less. Хз мне кажется мало, потому что чет не очень в тему предлагает по жанрам)

---
