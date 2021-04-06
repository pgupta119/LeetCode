# Given a sorted (in ascending order) integer array nums of n elements and a target value,
#  write a function to search target in nums. If target exists, then return its index, otherwise return -1.

#Example 
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4

class Solution:
    def search(self, nums, target):
        #declare a mid which has middle index of the array
        mid= int(len(nums)/2)
        # j has last index of the array
        j=len(nums)-1
        #i has first index of the array
        i=0
        #loop end when j become lesser than i
        while(j>=i):
            # case 1: when target element present at the mid
            if(target==nums[mid]):
                return mid
            #case 2 : find target element at the right side of the mid (target element has greater index than mid  index) 
            elif(nums[mid]<target):
                i=mid+1  
            #case 3 : find the target element at the left side of the mid
            else:
                j=(mid-1)
             
            #  New mid value with respect to  i and j value
            mid=int((i+j)/2) 
            
        return -1
    
a=Solution()
print(a.search([-1,0,3,5,9,12],9)
#output is 4
      




