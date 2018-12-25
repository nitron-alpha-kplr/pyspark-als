- r is now not rating but feedback data / interaction matrix (number of views, clicks, play count, time spent on a page, etc) - про диапазон значений r есть инфа в [original paper](http://yifanhu.net/PUB/cf.pdf) Раздел Preliminaries
- Короче, по идее ничего не нужно в коде менять. Просто подаешь свою interaction-matrix и добавляешь в `ALS`: 
- `implicitPrefs=False, alpha=1.0`  
- `alpha` - one more hyperparameter to tune. In the paper they found `alpha = 40` to work well and somewhere between `15 and 40 worked for other guy from medium`


https://spark.apache.org/docs/2.3.0/mllib-collaborative-filtering.html#tutorial

if the rating matrix is derived from another source of information (i.e. it is inferred from other signals), you can set implicitPrefs to True to get better results:

пока не до конца понял

[`суть`](https://youtu.be/58OjaDH2FI0?t=509)
