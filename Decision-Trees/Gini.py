# functions related to Gini Index

def gini_index(scr, grp_size, total_samples):
	if total_samples == 0:
		raise 'total_samples is 0'
	return (1.0 - scr) * (grp_size / total_samples)

def score(group, classes):
    s = 0
    if len(group) == 0:
        return s
    for class_val in classes:
        prop = [row[-1] for row in group].count(class_val) / len(group)
        s += prop * prop
    return s

def calc_total_gini(groups, classes, total_samples):
    t_gini = 0.0

    for group in groups:
        scr = score(group, classes)
        t_gini += gini_index(scr, len(group), total_samples)

    return t_gini

