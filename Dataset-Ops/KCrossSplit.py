from random import randrange

def cross_validation_split(dataset, n_folds):
    dataset_split = list()
    dataset_copy = list(dataset)
    fold_size = int(len(dataset) / n_folds)

    for i in range(n_folds):
        fold = list()
        while len(fold) < fold_size:
            to_append = randrange(len(dataset_copy))
            fold.append(dataset_copy.pop(to_append))
        dataset_split.append(fold)

    return dataset_split
