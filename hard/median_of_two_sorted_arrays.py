class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = []
        i = 0
        j = 0
        n = len(nums1)
        m = len(nums2)
        
        while i < n or j < m:
            if i < n and j < m:
                if nums1[i] > nums2[j]:
                    nums.append(nums2[j])
                    j += 1

                elif nums1[i] == nums2[j]:
                    nums.append(nums1[i])
                    nums.append(nums2[j])
                    i += 1
                    j += 1

                else:
                    nums.append(nums1[i])
                    i += 1
            
            elif i < n:
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1
            
        k = len(nums)
        if k % 2 == 0:
            p = k//2
            q = p-1
            
            return (nums[p]+nums[q])/2
        
        else:
            return nums[k//2]