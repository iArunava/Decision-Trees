import KCrossSplit as kcs
from predict import predict
import SplitXy
import DatasetHandler as dh
import TreeBuild as tb

def accuarcy_metric(actual, predicted):
    correct = 0
    for i in range(len(actual)):
        if actual[i] == predicted[i]:
            correct += 1
    return correct / float(len(actual)) * 100.0

def precision(tp, fp):
    return tp/(tp+fp)

def recall(tp, fn):
    return tp/(tp+fn)


def f1_score(actual, predicted):
    tp = 0.0
    fp = 0.0
    fn = 0.0
    tn = 0.0
    for i in range(len(actual)):
        if actual[i] == predicted[i] and actual[i] == '1':
            tp += 1
        if predicted[i] == '1' and actual[i] == '0':
            fp += 1
        if predicted[i] == '0' and actual[i] == '1':
            fn += 1
        if actual[i] == predicted[i] and actual[i] == '0':
            tn += 1

    prec = precision(tp, fp)
    rec  = recall (tp, fn)

    f1 = tp/(tp+((fn+fp)/2))
    return f1

def evaluate_kfold(dataset, process_dataset, max_depth, min_size, n_folds, *args):
    folds = kcs.cross_validation_split(dataset, n_folds)
    scores = list()

    for fold in folds:
        train_set = list(folds)
        train_set.remove(fold)
        train_set = sum(train_set, [])

        X_train, y_train = process_dataset(train_set)

        i = 0
        for row in X_train:
            row.append(y_train[i])
            i += 1

        node = tb.build_tree(X_train, max_depth, min_size)

        predicted = list()
        X_test, y_test = process_dataset(fold)

        for row in X_test:
            predicted.append(predict(node, row))

        accuracy = accuarcy_metric(actual=y_test, predicted=predicted)
        f1 = f1_score(y_test, predicted)
        scores.append({'accuracy':accuracy, 'F1_score':f1})

    return scores
