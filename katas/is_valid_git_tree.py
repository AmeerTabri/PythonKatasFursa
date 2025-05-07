import collections


def is_valid_git_tree(tree_map):
    all_nodes = set(tree_map.keys())
    children = set(node for children in tree_map.values() for node in children)
    roots = set(all_nodes - children)
    if len(roots) != 1:
        return False

    root = roots.pop()
    visited = set()
    queue = collections.deque([root])
    while queue:
        node = queue.pop()
        if node in visited:
            return False
        visited.add(node)
        for child in tree_map[node]:
            queue.append(child)

    return True


if __name__ == '__main__':
    valid_tree = {
        "A": ["B", "C"],
        "B": ["D"],
        "C": [],
        "D": []
    }

    invalid_tree = {
        "A": ["B"],
        "B": ["C"],
        "C": ["A"]  # cycle
    }

    print(f"Is valid tree: {is_valid_git_tree(valid_tree)}")  # Should be True
    print(f"Is valid tree: {is_valid_git_tree(invalid_tree)}")  # Should be False
