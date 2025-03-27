def removeDuplicates(self, nums):
    n = len(nums)
    k = 0
    for i in range(n):
        for j in range(i+1, n):
            if nums[j] == nums[i]:
                nums[j] = 101
    nums.sort()
    for i in range(n):
        if nums[i] == 101:
            del nums[i:]
            k = n - i
            break

removeDuplicates(self = 1, nums = [0,0,1,1,1,2,2,3,3,4])