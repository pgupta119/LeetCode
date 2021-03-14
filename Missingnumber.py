# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

# Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?

#Solution 1
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return (sum(range(1, len(nums)+1)) - sum(nums))


#Solution 2
class Solution:
    def missingNumber(self, nums):
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing