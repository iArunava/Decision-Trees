from csv import reader
import tree_build as tb

def load_csv(filename):
    file = open(filename, 'rb')
    lines = reader(file)
    dataset = list(lines)
    return dataset

dataset = load_csv('./dataset/titanic.csv')

def print_tree(node, depth=0):
    if isinstance(node, dict):
        print('%s[X%d < %.3f]' % ((depth*' ', (node['index']+1), node['value'])))
        print_tree(node['left'], depth+1)
        print_tree(node['right'], depth+1)
    else:
        print('%s[%s]' % ((depth*' ', node)))

tree = tb.build_tree(dataset, 3, 2)

print_tree(tree)

print (tree)
