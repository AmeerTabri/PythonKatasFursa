from collections import deque


# o(n) time solution
def max_sliding_window(nums, k):
    res = []
    dq = deque()

    for i in range(len(nums)):
        if dq and dq[0] < i - k + 1:
            dq.popleft()
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            res.append(nums[dq[0]])

    return res


if __name__ == '__main__':
    nums1 = [1, 3, -1, -3, 5, 3, 6, 7]
    k1 = 3

    result = max_sliding_window(nums1, k1)
    print(f"Sliding window maximums: {result}")  # Expected: [3, 3, 5, 5, 6, 7]

    # Additional test cases
    nums2 = [9, 11, 3, 4, 8, 7]
    k2 = 2
    result2 = max_sliding_window(nums2, k2)
    print(f"Sliding window maximums: {result2}")  # Expected: [11, 11, 4, 8, 8]

    nums3 = [1, -1]
    k3 = 1
    result3 = max_sliding_window(nums3, k3)
    print(f"Sliding window maximums: {result3}")  # Expected: [1, -1]
    