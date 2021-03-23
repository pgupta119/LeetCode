# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?


# Example 1:

# Input: nums = [2,2,1]
# Output: 1



#Solution
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x,y: x^y ,nums)   


#Solution

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return 2*sum(set(nums))-sum(nums)  