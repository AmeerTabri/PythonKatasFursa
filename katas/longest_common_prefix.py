def longest_common_prefix(strs):
    if not strs:
        return ""

    n = min([len(s) for s in strs])
    i = 0
    while i < n:
        for j in range(1, len(strs)):
            if strs[j][i] != strs[j-1][i]:
                return strs[0][:i]
        i += 1
    return strs[0][:i]


if __name__ == '__main__':
    test1 = ["flower", "flow", "flight"]
    test2 = ["dog", "racecar", "car"]
    test3 = ["interspecies", "interstellar", "interstate"]
    test4 = ["apple", "apricot", "ape"]

    print(f"Longest Common Prefix: {longest_common_prefix(test1)}")  # Output: "fl"
    print(f"Longest Common Prefix: {longest_common_prefix(test2)}")  # Output: ""
    print(f"Longest Common Prefix: {longest_common_prefix(test3)}")  # Output: "inter"
    print(f"Longest Common Prefix: {longest_common_prefix(test4)}")  # Output: "ap"