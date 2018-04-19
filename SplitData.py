import Gini as gini

def test_split(index, value, dataset):
    left, right = list(), list()

    for row in dataset:
        if row[index] < value:
            left.append(row)
        else:
            right.append(row)

    return left, right

def get_split(dataset):
    class_val = list(set(row[-1] for row in dataset))
    total_samples = len(dataset)
    c_index, c_value, c_score, c_groups = 999, 999, 999, None

    for index in range(len(dataset[0])-1):
        for row in dataset:
            groups = test_split(index, row[index], dataset)
            t_gini = gini.calc_total_gini(groups, class_val, total_samples)

            #print ('Attribute:', 'X'+str(index), ' Value:', row[index], ' Gini:', t_gini)

            if t_gini < c_score:
                c_index, c_value, c_score, c_groups = \
                                          index, row[index], t_gini, groups

    return {'index':c_index, 'value': c_value, 'groups':c_groups}
