# First Solution for Two Sum
nums = [3,2,4]
target = 6
count=0
for i in range(len(nums)):
    for j in range((i+1),len(nums)):
        if (nums[i]+nums[j]==target and count==0):
            print(i)
            print(j)



# Second Solution using Dictionary
            
class Solution(object):
   def twoSum(self, nums, target):
     
      dictionary = {}
      print(dictionary)
      for i in range(len(nums)):
         if target - nums[i] in dictionary:
            print(dictionary)
            return [dictionary[target - nums[i]],i]
         else:
            dictionary[nums[i]]=i
            print(dictionary)
input_list = [3,3,4]
ob1 = Solution()
print(ob1.twoSum(input_list, 6))   