from typing import List


def select_minimal_test_cases(test_cases: List[List[int]]) -> List[int]:
    all_requirements = set(r for case in test_cases for r in case)
    n = len(test_cases)

    def backtrack(start, path):
        covered = set()
        for idx in path:
            covered.update(test_cases[idx])
        if covered == all_requirements:
            return list(path)

        for i in range(start, n):
            result = backtrack(i + 1, path + [i])
            if result:
                return result
        return None

    # Try all sizes from 1 to n
    for size in range(1, n + 1):
        result = []

        def dfs(index, path):
            if len(path) == size:
                covered = set()
                for i in path:
                    covered.update(test_cases[i])
                if covered == all_requirements:
                    return path
                return None
            for i in range(index, n):
                res = dfs(i + 1, path + [i])
                if res:
                    return res
            return None

        result = dfs(0, [])
        if result:
            return result

    return []


if __name__ == "__main__":
    test_cases = [
        [1, 2, 3],
        [1, 4],
        [2, 3, 4],
        [1, 5],
        [3, 5]
    ]

    result = select_minimal_test_cases(test_cases)
    print(result)  # Expected output: [2, 3]
