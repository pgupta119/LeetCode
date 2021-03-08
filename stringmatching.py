
# Given an array of string words. Return all strings in words which is substring of another word in any order. 

# String words[i] is substring of words[j], if can be obtained removing some characters to left and/or right side of words[j].


#Example:
# Input: words = ["mass","as","hero","superhero"]
# Output: ["as","hero"]
# Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
# ["hero","as"] is also a valid answer.


#Solution 1
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        substring=[]
        for index_1,words_a in enumerate(words):
            for index_2, words_b in enumerate(words):
                if(index_1!=index_2 and words_a in words_b):
                    substring.append(words_a)
                    break
                
        return substring




#solution 2

lass Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        size = len( words )
        substr = set( words[i] for i in range(size) for j in range(size) if i != j and words[i] in words[j] )
        
        return [ *substr ]