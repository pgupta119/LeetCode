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



# Given an integer array nums where every element appears three times
#  except for one, which appears exactly once. Find the single element 
#  and return it.


# Example 1:

# Input: nums = [2,2,3,2]
# Output: 3


Solution:
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return int((3*sum(set(nums))-sum(nums))/2)