import tree_build as tb
import DatasetHandler as dh
import SplitXy

def print_tree(node, depth=0):
    if isinstance(node, dict):
        print('%s[X%d < %.3f]' % ((depth*' ', (node['index']+1), node['value'])))
        print_tree(node['left'], depth+1)
        print_tree(node['right'], depth+1)
    else:
        print('%s[%s]' % ((depth*' ', node)))

filename = './dataset/titanic.csv'
dataset = dh.read_csv(filename, headers=True)

X, y = SplitXy.splitXy(dataset, 0)

# Let's just drop the `Name` column and make a rough prediction
# The name column is at index `1`
X = dh.drop(X, column=1)
#X = dh.make_unique_columns_with(X, column=1)
print (dh.unique_values(X, column=0))
#print (X)

#tree = tb.build_tree(X, 10, 5)

#print_tree(tree)

#print (tree)
