"""
Given a list of integers numbers "nums".
You need to find a sub-array with length less equal to "k", with maximal sum.
The written function should return the sum of this sub-array.
Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    if k > len(nums):
        return 1, "Error: sub-array cannot be longer than the original array"

    max_ = nums[0]

    for i in range(len(nums) - k + 1):

        subarr = nums[i : i + k]
        for j in range(len(subarr)):
            if sum(subarr[j:]) > max_:
                max_ = sum(subarr[j:])

    return max_
