class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        idx1 = 0
        idx2 = 0

        res = []

        while idx1 < len(nums1) and idx2 < len(nums2):
            id1, val1 = nums1[idx1]
            id2, val2 = nums2[idx2]
            if id1 < id2:
                res.append(nums1[idx1])
                idx1 += 1
            elif id2 < id1:
                res.append(nums2[idx2])
                idx2 += 1
            else:
                res.append([id1, val1 + val2])
                idx1 += 1
                idx2 += 1

        while idx1 < len(nums1):
            res.append(nums1[idx1])
            idx1 += 1
        
        while idx2 < len(nums2):
            res.append(nums2[idx2])
            idx2 += 1
        
        return res

