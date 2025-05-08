from typing import List


def max_storage_area(containers: List[int]) -> int:
    left, right = 0, len(containers) - 1
    max_storage = 0

    while left < right:
        height, width = min(containers[left], containers[right]), right - left
        max_storage = max(max_storage, height * width)
        if containers[left] < containers[right]:
            left += 1
        else:
            right -= 1

    return max_storage


if __name__ == "__main__":
    containers = [2, 1, 5, 6, 2, 3]
    result = max_storage_area(containers)
    print("Max storage area:", result)  # Expected output: 10
