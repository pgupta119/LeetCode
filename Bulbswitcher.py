# There are n bulbs that are initially off. You first turn on all the bulbs, then you turn off every second bulb.

# On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). For the ith round, you toggle every i bulb. For the nth round, you only toggle the last bulb.

# Return the number of bulbs that are on after n rounds


# Input: n = 3
# Output: 1







# First try but time Exceeding
class Solution:
    def bulbSwitch(self, n: int) -> int:
        n=[True]*n
        count=len(n)
        if(len(n)==1):
            return 1
        while(i<=len(n)):
            if((i+1)%(j+1)==0):
                print(n[i])
                if(n[i]==True):
                    n[i]=False
                    print(n)
                    count=count-1
                else:
                    n[i]=True
                    count=count+1
        
        return count



#Second Soluion:
class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(n**(1/2))