def flatten_list(nested_list):
    if not isinstance(nested_list, list):
        return [nested_list]

    flattened_list = []
    for elem in nested_list:
        flattened_list += flatten_list(elem)

    return flattened_list


if __name__ == '__main__':
    nested_list = [
        1,
        [2, 3],
        [4, [5, 6]],
        7
    ]

    flat_list = flatten_list(nested_list)

    print(f"Flattened list: {flat_list}")  # Should be [1, 2, 3, 4, 5, 6, 7]
