import KCrossSplit as kcs

def accuarcy_metric(actual, predicted):
    correct = 0
    for i in range(len(actual)):
        if actual[i] == predicted[i]
            correct += 1
    return correct / float(len(actual)) * 100.0

def evaluate_kfold(dataset, algorithm, n_folds, *args):
    folds = kcs.cross_validation_split(dataset, n_folds)
    scores = list()

    for fold in folds:
        train_set = list(folds)
        train_set.remove(fold)
        train_set = sum(train_set, [])

        test_set = list()
        for row in fold:
            row_copy = list(row[:-1])
            test_set.append(row_copy)

        predicted = algorithm(train_set, test_set, *args)
        actual = [row[-1] for row in fold]

        accuracy = accuarcy_metric(actual=actual, predicted=predicted)
        scores.append(accuracy)

    return scores
