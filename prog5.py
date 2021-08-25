
def sort(nums):

    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j] > nums[j+1]:    #bubble sort
                temp=nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=temp

nums = [2,3,4,1,5,2,6,9,61,40,458,456,]

sort(nums)
print(nums)


