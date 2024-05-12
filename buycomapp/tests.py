#from django.test import TestCase

# Create your tests here.
nums=[0,1,2,2,3,0,4,2]
val=2
def removeElement(nums, val):
        lislen=len(nums)
        for i in range(lislen):
                if nums[i]==val:
                    print(nums[i])
                    nums.remove(nums[i])
                lislen=len(nums)-1
                print(lislen)

        print(nums)

removeElement(nums,val)