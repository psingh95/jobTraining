def two_numbers(nums, targetsum):
    """ for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] +nums[j] == targetsum:
                print(nums[i], nums[j]) """
    
    remain = []
    for i in range(len(nums)):
        if nums[i] in remain:
            print(nums[i],targetsum-nums[i])
        remain.append(targetsum-nums[i])



x = [1,2,3,4,5,6]
target = 6
two_numbers(x, target)
#o(n) and o(1)  