def splitXy(dataset, target_column=-1):
    if target_column < 0:
        target_column = len(dataset[0]) + target_column

    X = [row[:target_column]+row[target_column+1:] for row in dataset]
    y = [row[target_column] for row in dataset]

    return X, y
