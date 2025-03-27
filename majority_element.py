def majorityElement(self, nums):
    n = len(nums)
    m = 0
    k = 0
    nums.sort()
    print(nums, n, m, k)
    for i in range(n):
        k += 1
        for j in range(i+1, n):
            if nums[j] == nums[i]:
                k += 1
            else:
                if k >= m:
                    m = k
                k = 0
    print(nums, n, m, k)
majorityElement(self = 1, nums = [2,2,1,1,1,2,2])