# Given a sorted (in ascending order) integer array nums of n elements and a target value,
#  write a function to search target in nums. If target exists, then return its index, otherwise return -1.

#Example 

# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        mid= int(len(nums)/2)
        j=len(nums)-1
        i=0
        while(j>=i):
            if(target==nums[mid]):
                return mid
            elif(nums[mid]<target):
                i=mid+1  
            else:
                j=(mid-1)
                
            mid=int((i+j)/2) 
            
        return -1



