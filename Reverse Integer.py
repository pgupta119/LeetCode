#Reverse Integer
#Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
#inputs  Outputs
#123     321
#-123    -321
# -120   -21
# 0       0


class Solution:
    def reverse(self, x: int) -> int:
        if x>=0:
            sign=1
        else:
            sign=-1  
        temp,x=0,abs(x)
        while x:
            number = x%10
            x //= 10
            temp = temp*10 + number
        temp = temp * sign
        return temp if temp>=-2**31 and temp<=2**31-1 else 0
            