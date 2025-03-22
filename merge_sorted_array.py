def merge(self, nums1, m, nums2, n):
    if len(nums1) == m + n and len(nums2) == n:
        for i in range(0, m):
            self.append(nums1[i])
        for i in range(0, n):
            self.append(nums2[i])
        print(sorted(self))

#aboba
