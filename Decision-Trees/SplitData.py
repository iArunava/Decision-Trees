import Gini as gini

def test_split(index, value, dataset, weights):
    left, right = list(), list()
    left_weights, right_weights = list(), list()

    for row in dataset:
    for r in len(dataset):
        row = dataset[r]
        if row[index] < value:
            left.append(row)
            left_weights.append[weights[r]]
        else:
            right.append(row)
            right_weights.append[weights[r]]

    return left, right, left_weights, right_weights

def get_split(dataset, weights):
    class_val = list(set(row[-1] for row in dataset))
    total_samples = len(dataset)
    c_index, c_value, c_score, c_groups = 999, 999, 999, None

    for index in range(len(dataset[0])-1):
        for row in dataset:
            groups = test_split(index, row[index], dataset, weights.copy())
            w_groups = groups[2], groups[3]
            groups = groups[0], groups[1]
            t_gini = gini.calc_total_gini(groups, class_val, total_samples)

            #print ('Attribute:', 'X'+str(index), ' Value:', row[index], ' Gini:', t_gini)

            if t_gini < c_score:
                c_index, c_value, c_score, c_groups = \
                                          index, row[index], t_gini, groups
                weight_grp = w_groups

    return {'index':c_index, 'value': c_value, 'groups':c_groups, 'weights':weight_grp}
