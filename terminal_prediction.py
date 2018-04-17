# this file stores functions that predicts classes given the group in the terminal node

terminal_pred(group):
    preds = [row[-1] for row in group]
    return max(preds, key=preds.count)


