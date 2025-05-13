def compare_versions(version1, version2):
    list1 = [int(elem) for elem in version1.split('.')]
    list2 = [int(elem) for elem in version2.split('.')]

    i = 0
    while i < min((len(list1), len(list2))):
        if list1[i] > list2[i]:
            return 1
        elif list1[i] < list2[i]:
            return -1
        i += 1

    for j in range(i, len(list1)):
        if list1[j] > 0:
            return 1

    for j in range(i, len(list2)):
        if list2[j] > 0:
            return -1

    return 0


if __name__ == '__main__':
    print(f"'1.0.0' compared to '1.0.1': {compare_versions('1.0.0', '1.0.1')}")  # Expected: -1
    print(f"'2.1.0' compared to '1.9.9': {compare_versions('2.1.0', '1.9.9')}")  # Expected: 1
    print(f"'1.2.3' compared to '1.2.3': {compare_versions('1.2.3', '1.2.3')}")  # Expected: 0

    # Additional test cases
    print(f"'1.2' compared to '1.2.0': {compare_versions('1.2', '1.2.0')}")  # Expected: 0
    print(f"'1.10.0' compared to '1.2.0': {compare_versions('1.10.0', '1.2.0')}")  # Expected: 1
    print(f"'2.0.0' compared to '10.0.0': {compare_versions('2.0.0', '10.0.0')}")  # Expected: -1