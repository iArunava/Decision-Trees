import numpy as np
import pandas as pd
import gini
import split_data

def calc_total_gini(groups, classes, total_samples):
    t_gini = 0.0

    for group in groups:
        score = gini.score(group, classes)
        t_gini += gini.gini_index(score, len(group), total_samples)

    return t_gini

def get_split(dataset):
    class_val = list(set(row[-1] for row in dataset))
    total_samples = len(dataset)
    c_index, c_value, c_score, c_groups = 999, 999, 999, None

    for index in range(len(dataset[0])-1):
        for row in dataset:
            groups = split_data.test_split(index, row[index], dataset)
            t_gini = calc_total_gini(groups, class_val, total_samples)

            print ('Attribute:', 'X'+str(index), ' Value:', row[index], ' Gini:', t_gini)

            if t_gini < c_score:
                c_index, c_value, c_score, c_groups = \
                                          index, row[index], t_gini, groups
                
    return {'index':c_index, 'value': c_value, 'groups':c_groups}
