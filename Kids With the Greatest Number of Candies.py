#Given the array candies and the integer extraCandies, 
# where candies[i] represents the number of candies that the ith kid has.

#For each kid check if there is a way to distribute extraCandies among 
# the kids such that he or she can have the greatest number of candies among them. 
# Notice that multiple kids can have the greatest number of candies.

#Example 
#Input: candies = [2,3,5,1,3], extraCandies = 3
# Output: [true,true,true,false,true] 
# Explanation: 
# Kid 1 has 2 candies and if he or she receives all extra candies (3) will have 5 candies --- the greatest number of candies among the kids. 
# Kid 2 has 3 candies and if he or she receives at least 2 extra candies will have the greatest number of candies among the kids. 
# Kid 3 has 5 candies and this is already the greatest number of candies among the kids. 
# Kid 4 has 1 candy and even if he or she receives all extra candies will only have 4 candies. 
# Kid 5 has 3 candies and if he or she receives at least 2 extra candies will have the greatest number of candies among the kids. 

# Example :
#Input: candies = [12,1,12], extraCandies = 10
#Output: [true,false,true]

#My Approach is  to take a new empty list where we can store the bool value. The current index value of the candies 
#is added with extra candies which and then compare every new temp value  with the  max value if the maximum value is equal and less than
# then it will Insert "True" Value in the n Output list

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        output=[]       
        for i in candies:
            temp=i+extraCandies
            if(temp>=max(candies)):
                output.append(True)
            else:
                output.append(False)
            
        return output



#Second Solution with shorter code

def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
	maxCandies = max(candies)
	return [candy+extraCandies >= maxCandies for candy in candies]
