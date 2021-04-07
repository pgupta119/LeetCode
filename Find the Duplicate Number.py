# # Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
# There is only one repeated number in nums, return this repeated number.


# Example
# Input: nums = [1,3,4,2,2]
# Output: 2

#Solution 1
class Solution:
    def findDuplicate(self,nums):
        #checking for element and if it present more than one times in the list the count becomes 2 and that will be the output
        for i in nums:
            count=0
            for j in nums :
                if (i==j):
                    count= count +1
                    if(count==2):
                        return i


#comment : This will work for small value of the list
print(Solution.findDuplicate([1,3,4,2,2]))


