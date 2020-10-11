# Given an unsorted integer array, find the smallest missing positive integer.

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 0: return 1
        if n == 1: return 2 if nums[0] == 1 else 1

        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1

        for i in range(n):
            val = abs(nums[i])
            if val <= n and nums[val-1] > 0:
                nums[val-1] *= -1

        for i in range(n):
            if nums[i] > 0:
                return i + 1

        return n + 1
