# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

#Example

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

#Solution;

class Solution:
    def maxProfit(self, prices):
        #Initially maximum difference is zero
        max_diff=0
        # Initialize the maximum  of the array at the last index.
        max_number=prices[-1]
        # loop for checking the maximum difference and assign maximum value
        for j in range(len(prices)-2,-1,-1):
            # if current index value is greater than max_number then assign the current value to max_number
            if(prices[j]>max_number):
                max_number=prices[j]
                # otherwise take the difference of max_number and current value,and compare with max_difference which provide max value usin max function
            else:
                max_diff= max (max_diff,(max_number-prices[j]))
        #return the max difference after execution of the loop
        return max_diff
  
sol=Solution()
print(sol.maxProfit([7,1,5,3,6,4]))

#output should be 5
