# Decision-Trees

This repository is my implementation of Decision Trees from scratch. 
No use of Machine Learning libraries. I even skipped on Pandas and Numpy.
So, basically everything is from scratch.

Sure the algorithm can be tuned at a lot of places for better results.
But, the point of this implementation is to get a clear idea about how the algorithm works :)

That said, I plan on improving my code as I learn new techniques.

# Accuracy and F1_Score

Using KCrossValidation using 3 folds on the `banknote` dataset, this is the output

![results_decision_trees](https://user-images.githubusercontent.com/26242097/39419825-47ce3a68-4c7f-11e8-97bf-6e56d1dd6627.png)


NOTE: Data preprocessing is not taken much into account

# How to use

1) Clone the repo

```
git clone https://github.com/iArunava/Decision-Trees.git
```

2) Move into the cloned repo

```
cd Decision-Trees
```

3) Run the `main.py` file

```
python3 main.py
```

4) You can pass the `max_depth=` and `min_size=` as arguments while calling the `main.py` file. 

```
python3 main.py 12 10
```

NOTE: `max_depth` is the first argument and `min_size` is the second argument.\n
NOTE: Missing one argument will set default arguments for `max_depth` and `min_size` with a warning shown.

# LICENSE 

Distributed under MIT.
Have fun!
