def removeElement(self, nums, val):
    k = len(nums)
    l = []
    for i in range(len(nums)):
        if nums[i] == val:
            nums[i] = -1
            k -= 1
    nums.sort(reverse = True)
    for i in range(len(nums)):
        if nums[i] >= 0:
            l.append(nums[i])
    nums = l
    print()
removeElement(self = 1, nums = [3,2,2,3], val = 3)