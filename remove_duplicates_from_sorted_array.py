def removeDuplicates(self, nums):
    new_nums = []
    for i in range(len(nums)):
        if i == 0:
            new_nums.append(nums[i])
            continue
        if nums[i] != nums[i-1]:
            new_nums.append(nums[i])
    nums = new_nums
    k = len(nums)
    print(k, nums)

removeDuplicates(self = 1, nums = [0,0,1,1,1,2,2,3,3,4])