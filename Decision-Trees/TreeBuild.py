import SplitData as sd
import RecursiveSplitting as rs

def build_tree(train, max_depth, min_size, weights):
    root = sd.get_split(train, weights)
    rs.recursive_split(root, 1, max_depth, min_size)
    return root
