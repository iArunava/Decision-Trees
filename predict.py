def predict(node, row):
    if row[node['index']] < node['value']:
        if isinstance(node['left'], dict):
            predict(node['left'], row)
        else:
            return node['left']

    else:
        if isinstance(node['right'], dict):
            predict(node['right'], row)
        else:
            return node['right']
