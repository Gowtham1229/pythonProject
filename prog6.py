

def sort(nums):

    for i in range(9):
        minpos = i
        for j in range(i,10):
            if nums[j] < nums[minpos]:
                minpos = j
                                            #selesction sort
                temp = nums[i]
                nums[i] = nums[minpos]
                nums[minpos] = temp
               # print(nums)
nums = [20,19,18,17,16,15,14,13,12,11]
sort(nums)

print(nums)