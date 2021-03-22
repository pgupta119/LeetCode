count=0
a=[7,2,9,4,5,2,5,8,3,1,9]
n=0
while(n<len(a)):
    i=n
    if a[i]<a[i+1] or a[i]<a[i+2]:
        if a[i+1]<a[i+2]:
            i=i+1
        elif a[i]<a[i+2]:
            i=i+2
        count +=1
    print(max(count))