def test_split(index, value, dataset):
    left, right = list(), list()

    for row in dataset:
        if row[index] < value:
            left.append(row)
        else:
            right.append(row)

    return left, right
