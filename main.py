import numpy as np
import pandas as pd
import tree_build as tb

## TODO: This will not work as dataset is a DataFrame Object so handle that
# dataset = pd.read_csv('./dataset/titanic.csv')

dataset = [[2.771244718,1.784783929,0],
    [1.728571309,1.169761413,0],
        [3.678319846,2.81281357,0],
            [3.961043357,2.61995032,0],
                [2.999208922,2.209014212,0],
                    [7.497545867,3.162953546,1],
                        [9.00220326,3.339047188,1],
                            [7.444542326,0.476683375,1],
                                [10.12493903,3.234550982,1],
                                    [6.642287351,3.319983761,1]]



def print_tree(node, depth=0):
    if isinstance(node, dict):
        print('%s[X%d < %.3f]' % ((depth*' ', (node['index']+1), node['value'])))
        print_tree(node['left'], depth+1)
        print_tree(node['right'], depth+1)
    else:
        print('%s[%s]' % ((depth*' ', node)))

tree = tb.build_tree(dataset, 1, 2)

print_tree(tree)
