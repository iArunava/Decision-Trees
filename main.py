import gini

def calc_total_gini(groups, classes):
	total_samples = sum([len(grp) for grp in groups])
	t_gini = 0.0

	for group in groups:
		score = gini.score(group, classes)
		t_gini += gini.gini_index(score, len(group), total_samples)
	
	return t_gini

print (calc_total_gini([[[1, 1], [1, 0]], [[1, 1], [1, 0]]], [0, 1]))
print (calc_total_gini([[[1, 0], [1, 0]], [[1, 1], [1, 1]]], [0, 1]))

