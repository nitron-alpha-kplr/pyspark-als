# pyspark-als
Alternating Least Squares (ALS) matrix factorization using pyspark


maxIter - as rule of thumb: if `abs(metric[i]` - `metric[i - 1]) < 0.001` - stop iteration  
Ну bigger is better, точнее матрица разлагается  
[Тут пишут](https://spark.apache.org/docs/latest/mllib-collaborative-filtering.html), что ALS typically converges to a reasonable solution in 20 iterations or less. Хз мне кажется мало, потому что чет не очень в тему предлагает по жанрам)

---


---

grouplens dataset contains explicit ratings  
but my real dataset is implicit feedback data  
so I use implicit here for code consistency  
the only difference is `implicitPrefs=True` and additional `alpha` parameter

также графики тоже стремные, потому что я юзаю implicit, хотя данные explicit. Делаю так потому чтобы code consistency был

в принципе можно просто grouplens dataset отскейлить, но пофиг


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
</details>

----------------------------------------------------------------
