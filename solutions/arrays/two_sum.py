# LeetCode Problem: 1. Two Sum
# Difficulty: Easy
# Approach: Hash Map
# Time: O(n), Space: O(n)

class Solution:
    def twoSum(self, nums, target):
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
