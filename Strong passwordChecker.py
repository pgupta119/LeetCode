# #A password is considered strong if the below conditions are all met:

# It has at least 6 characters and at most 20 characters.
# It contains at least one lowercase letter, at least one uppercase letter, and at least one digit.
# It does not contain three repeating characters in a row (i.e., "...aaa..." is weak, but "...aa...a..." is strong, assuming other conditions are met).
# Given a string password, return the minimum number of steps required to make password strong. if password is already strong, return 0.

# In one step, you can:

# Insert one character to password,
# Delete one character from password, or
# Replace one character of password with another character.



class Solution:
    def strongPasswordChecker(self,password : str)-> int:
        if (len(password)<2)):
            return 6- len(password)


        lowercase=0
        uppercase=0
        number=0
        repeat=0
        if (len(password>6) and len(password)<20):
            for i in len(password):
                if (password[i] >='A'  and password[i]<='Z'):
                    lowercase =lowercase+1
                if (password[i]>='a' and password[i]<='z'):
                    uppercase =uppercase +1
                if (password[i]>=0 and password[i]<=9):
                    number =number+1


            for j in len(password):
                if(password[j]==password[j+1]):
                    repeat=repeat +1

            if(lowercase>=1 and uppercase>=1 and number=>1):
                return 
                
