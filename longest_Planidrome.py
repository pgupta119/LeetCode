#Given a string s, return the longest palindromic substring in s.

#Example 1
#Input: s = "babad"
#Output: "bab"
#Note: "aba" is also a valid answer

# Example 2
#Input: s = "cbbd"
#Output: "bb"

#Example 3
#Input: s = "a"
#Output: "a"

#Example 4
#Input: s = "ac"
#Output: "a"


# My Approach is select middle and check both side of the (left and right)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def side(l,r):
            while (l>=0 and r<len(s) and s[l]==s[r]):
                l-=1
                r+=1
            return s[l+1:r]
                   
        result=""
        for i in range(len(s)):
                   test=side(i,i)
                   if len(test)>len(result): result=test
                   test=side(i,i+1)
                   if len(test)>len(result): result =test
                   
        return result
