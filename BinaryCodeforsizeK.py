# Given a binary string s and an integer k.

# Return True if every binary code of length k is a substring of s. Otherwise, return False.

#example:
# Input: s = "00110110", k = 2
# Output: true
# Explanation: The binary codes of length 2 are "00", "01", "10" and "11". They can be all found as substrings at indicies 0, 1, 3 and 2 respectively.




class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        substring=2**k
        N=len(s)
        unique=set([s[i:i+k] for i in range(N+1-k)])
        return substring==len(unique)