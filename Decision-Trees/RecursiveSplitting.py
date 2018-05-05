from predict import terminal_pred
import SplitData as sd

def recursive_split(node, depth, max_depth, min_size, ignore=''):
    left, right = node['groups']
    del (node['groups'])

    left_keep, right_keep = True, True

    # When split causes all items to be either in left or right
    if not left or not right:
        ter_pred = terminal_pred(left + right, node['weights'][0] + node['weights'][1], node, ['left', 'right'])
        return ter_pred[1], ter_pred[1]

    # Check for the max_depth
    if depth >= max_depth:
        ter_pred = terminal_pred(left, node['weights'][0], node, ['left'])
        left_keep = ter_pred[1]

        ter_pred = terminal_pred(right, node['weights'][1], node, ['right'])
        right_keep = ter_pred[1]

        # TODO: Just checking the right split (need to check the left split)
        return left_keep, right_keep

    # left-child
    if len(left) <= min_size:
        left_keep = evaluate_terminal(left, node['weights'][0], node, ['left'])
    else:
        node['left'] = sd.get_split(left)
        rec_splitted = recursive_split(node['left'], depth+1, max_depth, min_size)
        # TODO: Handle the case if any splitted node evaluates False

    # right-child
    if len(right) <= min_size:
        right_keep = evaluate_terminal(right, node['weights'][1], node, ['right'])
    else:
        node['right'] = sd.get_split(right)
        rec_splitted = recursive_split(node['right'], depth+1, max_depth, min_size)
        # TODO: Handle the case if any splitted node evaluates False

    return left_keep, right_keep

def evaluate_terminal(dataset, weights, node, childs):
    ter_pred = terminal_pred(dataset, weights)
    if ter_pred[1] == False:
        return False
    for child in childs:
        node[child] = ter_pred[0]
    return True
