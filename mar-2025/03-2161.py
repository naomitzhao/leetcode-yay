class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        less = []
        equalCount = 0
        more = []

        for num in nums:
            if num < pivot:
                less.append(num)
            elif num > pivot:
                more.append(num)
            else:
                equalCount += 1
        
        res  = less + [pivot] * equalCount + more
        return res
