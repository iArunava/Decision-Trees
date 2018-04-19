from predict import terminal_pred
import SplitData as sd

def recursive_split(node, depth, max_depth, min_size, ignore=''):
    left, right = node['groups']
    del (node['groups'])

    # When split causes all items to be either in left or right
    if not left or not right:
        node['left'] = node['right'] = terminal_pred(left + right)
        return

    # Check for the max_depth
    if depth >= max_depth:
        node['left'] = terminal_pred(left)
        node['right'] = terminal_pred(right)
        return

    # left-child
    if len(left) <= min_size:
        node['left'] = terminal_pred(left)
    else:
        node['left'] = sd.get_split(left)
        recursive_split(node['left'], depth+1, max_depth, min_size)

    # right-child
    if len(right) <= min_size:
        node['right'] = terminal_pred(right)
    else:
        node['right'] = sd.get_split(right)
        recursive_split(node['right'], depth+1, max_depth, min_size)
