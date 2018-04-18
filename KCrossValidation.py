import KCrossSplit as kcs
from predict import predict
import SplitXy
import DatasetHandler as dh
import tree_build as tb

def accuarcy_metric(actual, predicted):
    correct = 0
    for i in range(len(actual)):
        if actual[i] == predicted[i]:
            correct += 1
    return correct / float(len(actual)) * 100.0

def evaluate_kfold(dataset, process_titanic, n_folds, *args):
    folds = kcs.cross_validation_split(dataset, n_folds)
    scores = list()

    for fold in folds:
        train_set = list(folds)
        train_set.remove(fold)
        train_set = sum(train_set, [])

        X_train, y_train = process_titanic(train_set)

        '''
        test_set = list()
        for row in fold:
            row_copy = list(row[:-1])
            test_set.append(row_copy)
        '''

        i = 0
        for row in X_train:
            row.append(y_train[i])
            i += 1

        node = tb.build_tree(X_train, 15, 10)

        predicted = list()
        X_test, y_test = process_titanic(fold)

        #X_test = X_test[:5]
        #y_test = y_test[:5]
        for row in X_test:
            predicted.append(predict(node, row))

        y_test = ['0']*len(X_test)
        accuracy = accuarcy_metric(actual=y_test, predicted=predicted)
        scores.append(accuracy)

        print (y_test)
        print (predicted)
        print (node)
    return scores
