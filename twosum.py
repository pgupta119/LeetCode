#Problem Statement:
#Given an array of integers, find two numbers such that they add up to a specific target number.
##
##The function twoSum should return indices of the two numbers such that they add up to the target,
##where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.
##
##You may assume that each input would have exactly one solution.
##
##Input: numbers={2, 7, 11, 15}, target=9
##Output: index1=1, index2=2

# First Solution for Two Sum

class Solution():
   def twoSum(self, nums, target):
      # first loop is for each element is sum with(Second loop) each element and check the sum is equal to target number
        for i in range(len(nums)):
            for j in range((i+1),len(nums)):
                if (nums[i]+nums[j]==target):
                    return(i,j)
               
               
print(Solution.twoSum([2,7,11,15],9))



# Second Solution using Dictionary
            
class Solution():
   def twoSum(self, nums, target):
     
      dictionary = {}
      #initialize the dictionary
      for i in range(len(nums)):
         if target - nums[i] in dictionary:
            return [dictionary[target - nums[i]],i]
         else:
            dictionary[nums[i]]=i
print(Solution.twoSum({2,7,11,15},9))
            
