# Given two strings a and b, return true if you can swap two letters in a so the result is equal to b, otherwise, return false.

# Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at a[i] and b[j]. For example, swapping at indices 0 and 2 in "abcd" results in "cbad".


#Example 

# Input: a = "ab", b = "ba"
# Output: true
# Explanation: You can swap a[0] = 'a' and a[1] = 'b' to get "ba", which is equal to b.





class Solution:
    def buddyStrings(self, a: str, b: str) -> bool:
        if len(a)!= len(b): return False
        if a==b and len(set(a))!=len(a):
            return True
        indices,indices1=[],[]
        for i in range(len(a)):
            if a[i] != b[i]:
                indices.append(a[i])
                indices1.append(b[i])
        return len(indices)==2 and indices==indices1[::-1]