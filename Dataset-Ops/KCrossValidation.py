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
        scores.append(accuracy)

    return scores
