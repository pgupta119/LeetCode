# An integer is a palindrome when it reads the same backward as forward. 
# For example, 121 is palindrome while 123 is not.

 #solution 1
class Solution:
    def isPalindrome(self, x: int) -> bool:
        sum=0
        z=x
        while(x>0):
            temp=x%10
            print(temp)
            sum=sum*10+temp
            x=x//10
            
        if (z==sum or x==0):
            print(sum)
            return True
        else:
            print(sum)
            return False


#Solution 2

 class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x)==str(x)[::-1]


#Solution 3

 class Solution:
    def isPalindrome(self, x: int) -> bool:
        return False if x<0 else x==int(str(x)[::-1])
