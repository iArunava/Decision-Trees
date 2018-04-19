import sys
sys.path.insert(0, './Dataset-Ops/')
sys.path.insert(1, './Decision-Trees')

import DatasetHandler as dh
import KCrossValidation as kcv
import SplitXy

def process_dataset(train_set):
    X_train, y_train = SplitXy.splitXy(train_set, 0)

    # Let's just drop the `Name` column and make a rough prediction
    # The name column is at index `1`
    X_train = dh.drop(X_train, column=1)
    X_train = dh.make_unique_columns_with(X_train, column=1)
    for i in range(5):
        X_train = dh.str_col_float(X_train, i)
    return X_train, y_train

filename = './dataset/titanic.csv'
dataset = dh.read_csv(filename, headers=True)


print (kcv.evaluate_kfold(dataset, process_dataset, max_depth=9, min_size=8, n_folds=3))
