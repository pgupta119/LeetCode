Author  Prakash Gupta
class Solution:
    def BinarySearch( num list: target int) > int:
        mid=int(len(nums)/2)
        end=len(nums)-1
        start=0
        while(end>start):
            if(target==nums[mid]):
                return mid
            else:
                if(target>nums[mid]):
                    i=mid+1
                else:
                    j=mid-1
            mid=int((i+j)/2)
        return -1


