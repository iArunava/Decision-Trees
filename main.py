import tree_build as tb
import DatasetHandler as dh
import SplitXy
import KCrossValidation as kcv

def process_titanic(train_set):
    X_train, y_train = SplitXy.splitXy(train_set, 0)

    # Let's just drop the `Name` column and make a rough prediction
    # The name column is at index `1`
    X_train = dh.drop(X_train, column=1)
    X_train = dh.make_unique_columns_with(X_train, column=1)
    for i in range(5):
        X_train = dh.str_col_float(X_train, i)
    return X_train, y_train
    
def print_tree(node, depth=0):
    if isinstance(node, dict):
        print('%s[X%d < %.3f]' % ((depth*' ', (node['index']+1), node['value'])))
        print_tree(node['left'], depth+1)
        print_tree(node['right'], depth+1)
    else:
        print('%s[%s]' % ((depth*' ', node)))

filename = './dataset/titanic.csv'
dataset = dh.read_csv(filename, headers=True)



#print (dh.unique_values(X, column=0))

print (kcv.evaluate_kfold(dataset, process_titanic, 3))
#tree = tb.build_tree(X, 10, 5)

#print_tree(tree)

#print (tree)
