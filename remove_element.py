def removeElement(self, nums, val):
    n = len(nums)
    for i in range(n):
        if nums[i] == val:
            nums[i] = -1
    nums.sort(reverse=True)
    print(nums)
    for i in range(n):
        if nums[i] == -1:
            del nums[i:]
            break
    print(nums)
removeElement(self = 1, nums = [3,2,2,3], val = 3)