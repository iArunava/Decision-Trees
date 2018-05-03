import TreeBuild as tb
from predcit import predcit
import math

def adaboost(dataset, process_dataset, rounds=10):
    X_train, y_train = process_dataset(dataset)

    # Changing output of negetive samples from `0` to `-1`
    for i in range(len(y_train)):
        if not y_train[i]:
            y_train[i] = -1

    # Initial weights on each sample
    weights = [1/len(X_train)] * len(X_train)
    trees = list()
    alpha_m = list()

    # Rounds
    for r in range(rounds):
        trees.append(tb.build_tree(X_train, 1, 500))

        # Computing the error in round r
        sum_num = 0
        sum_weights = sum(weights)
        preds = list()
        for i in range(len(X_train)):
            preds.append(1 if predcit(trees[r], X_train[i]) == y_train[i] else -1)
            sum_num += weights[i] * preds[i]

        e_t = sum_num / sum_weights

        # Calculating alpha_m
        alpha_m.append(0.5 * math.log(((1-e_t)/e_t), 2))

        # Updating weights
        norm_t = list()
        for i in range(len(y_train)):
            norm_t.append(weights[i] * math.exp(-alpha_m[r] * y_train[i] * preds[i]))
        norm_t_sum = sum(norm_t)
        for i in range(len(y_train)):
            weights[i] = (weights[i] * norm_t[i]) / norm_t_sum

    return alpha_m, trees

def ada_predict(alpha_m, trees, row):
    sum_t = 0
    for t in range(rounds):
        sum_t += alpha_m[t]*predcit(trees[t], row)
    return 1 if sign(sum_t) else 0

def sign(num):
    if num < 0:
        return -1
    elif num == 0:
        return 0
    elif num > 0:
        return 1
