def palindrome(string):
    odd_times=0
    for i in range(0,len(string)):
        count=0
        for j in range(0,len(string)):
            if(string[i]==string[j]):
                count= count+1
                print(count)
                
        if ( count%2==1):
            odd_times=odd_times+1
            print("odd_times",odd_times)

        
    if (odd_times>1):
        return "No"
        
    else:
        return "Yes"

string=palindrome("geeksos")
print(string)



