tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': ['G'],
    'G': []
}

def dls_tree(tree, current, goal, depth, path):
    if current == goal:
        return path

    if depth == 0:
        return None

    for neighbor in tree.get(current, []):
        result = dls_tree(tree, neighbor, goal, depth - 1, path + [neighbor])
        if result is not None:
            return result

    return None


def iddfs_tree(tree, start, goal, max_depth):
    for depth in range(max_depth + 1):
        result = dls_tree(tree, start, goal, depth, [start])
        if result is not None:
            return result
    return None


print("IDDFS on TREE:")
print(iddfs_tree(tree, 'A', 'G', 5))
tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': ['G'],
    'G': []
}

def dls_tree(tree, current, goal, depth, path):
    if current == goal:
        return path

    if depth == 0:
        return None

    for neighbor in tree.get(current, []):
        result = dls_tree(tree, neighbor, goal, depth - 1, path + [neighbor])
        if result is not None:
            return result

    return None


def iddfs_tree(tree, start, goal, max_depth):
    for depth in range(max_depth + 1):
        result = dls_tree(tree, start, goal, depth, [start])
        if result is not None:
            return result
    return None


print("IDDFS on TREE:")
print(iddfs_tree(tree, 'A', 'G', 5))
