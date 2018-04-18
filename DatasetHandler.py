from csv import reader

def read_csv(filename, headers=False):
    file = open(filename, 'r')
    lines = reader(file)
    print (lines)
    dataset = list(lines)
    file.close()

    if headers:
        dataset = dataset[1:]

    return dataset

def drop(dataset, column):
    dataset = [row[:column]+row[column+1:] for row in dataset]
    return dataset

def unique_values(dataset, column):
    '''
    uv_list   -> Contains the unique values

    instances -> Contains the number of instances of each unique value.
              -> It works like:
              -> The unique value uv_list[i] has number of instances
              -> equal to instances[i]

    uv_dict   -> Key:Value pairs
              -> where, Key = unique value
              -> Value = Column number of that unique value

    uv_val    -> Number of unique values in column
    '''
    uv_list = list()
    instances = list()
    uv_dict = dict()
    uv_val = 0
    temp = 0
    run = 0

    for row in dataset:
        try:
            temp = uv_dict[row[column]]
            instances[temp] += 1
        except KeyError:
            uv_dict[row[column]] = uv_val
            uv_list.append(row[column])
            instances.append(1)
            uv_val += 1

    return uv_list, instances, uv_dict, uv_val

def make_unique_columns_with(ds, column, drop=True):
    uvalues = unique_values(ds, column)
