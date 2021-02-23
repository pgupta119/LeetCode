#Palindrome Series
a=123215
temp=a
sum=0
while (temp>0):
    rem= temp % 10
    sum =sum*10 +rem
    temp=temp//10
if (sum==a):
    print("palidrome")
else:
    print("Not Palidome")

