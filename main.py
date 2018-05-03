import sys
sys.path.insert(0, './Dataset-Ops/')
sys.path.insert(1, './Decision-Trees')
sys.path.insert(2, './AdaBoost')

import DatasetHandler as dh
import KCrossValidation as kcv
import SplitXy
import warnings
import adaboost as ab

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

# First argument: 1 -> Using K-fold
#                 2 -> AdaBoost
# Second Argument is max_depth
# Third Argument is min_size
max_depth = 0
min_size  = 0
folds = 3
required_arguments = 1

try:
    method = sys.argv[1]
except IndexError:
    print ('Requried first argument missing\n' \
          'use `1` to evaluate model using k-folds\n' \
          'use `2` to evaluate model using AdaBoost\n\n' \
          'Exiting program.')
    exit(0)

try:
    max_depth = int(sys.argv[required_arguments+1])
    min_size = int(sys.argv[required_arguments+2])

    print ('Using:\nmax_depth =', max_depth, '\nmin_size =', min_size, '\n')

except IndexError:
    warnings.warn('NOTE: One of the arguments is missing\nUsing Default parameters ' \
                  'for both max_depth and min_size\nSetting:\nmax_depth = 9\nmin_size = 8\n', stacklevel=2)
    max_depth = 9
    min_size = 8

if sys.argv[1] == '1':
    acc_f1_list =  kcv.evaluate_kfold(dataset, process_dataset_banknote, max_depth=max_depth, min_size=min_size, n_folds=folds)

    i = 1
    for acc_f1 in acc_f1_list:
        print ('Iteration', i)
        print ('\tAccuracy: ', acc_f1['accuracy'])
        print ('\tF1 Score: ', acc_f1['F1_score'])
        i += 1
elif sys.argv[1] == '2':
    # Use adaboost
    ab.adaboost(dataset, process_dataset_banknote)
