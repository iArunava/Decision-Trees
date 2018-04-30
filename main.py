import sys
sys.path.insert(0, './Dataset-Ops/')
sys.path.insert(1, './Decision-Trees')

import DatasetHandler as dh
import KCrossValidation as kcv
import SplitXy
import warnings

def process_dataset_titanic(train_set):
    X_train, y_train = SplitXy.splitXy(train_set, 0)

    # Let's just drop the `Name` column and make a rough prediction
    # The name column is at index `1`
    X_train = dh.drop(X_train, column=1)
    X_train = dh.make_unique_columns_with(X_train, column=1)
    for i in range(5):
        X_train = dh.str_col_float(X_train, i)
    return X_train, y_train

def process_dataset_banknote(dataset):
    X_train, y_train = SplitXy.splitXy(dataset)
    return X_train, y_train

#filename = './dataset/titanic.csv'
filename = './dataset/banknote.csv'
dataset = dh.read_csv(filename, headers=False)

# First Argument is max_depth
# Second Argument is min_size
max_depth = 0
min_size  = 0
folds = 3

try:
    max_depth = int(sys.argv[1])
    min_size = int(sys.argv[2])

    print ('Using:\nmax_depth =', max_depth, '\nmin_size =', min_size, '\n')

except IndexError:
    warnings.warn('NOTE: One of the arguments is missing\nUsing Default parameters ' \
                  'for both max_depth and min_size\nSetting:\nmax_depth = 9\nmin_size = 8\n', stacklevel=2)
    max_depth = 9
    min_size = 8

acc_f1_list =  kcv.evaluate_kfold(dataset, process_dataset_banknote, max_depth=max_depth, min_size=min_size, n_folds=folds)

i = 1
for acc_f1 in acc_f1_list:
    print ('Iteration', i)
    print ('\tAccuracy: ', acc_f1['accuracy'])
    print ('\tF1 Score: ', acc_f1['F1_score'])
    i += 1
