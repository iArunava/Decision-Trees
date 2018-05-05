def predict(node, row):
    if row[node['index']] < node['value']:
        if isinstance(node['left'], dict):
            return predict(node['left'], row)
        else:
            return node['left']

    else:
        if isinstance(node['right'], dict):
            return predict(node['right'], row)
        else:
            return node['right']


def terminal_pred(group, weights):
    keep = True
    preds = [row[-1] for row in group]
    sum_w = sum(weights)
    if sum_w <= 0:
        keep = False
    return max(preds, key=preds.count), keep
