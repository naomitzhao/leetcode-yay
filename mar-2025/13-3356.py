class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        left = 0
        right = len(queries)

        if not self.successfulQueries(right, nums, queries):
            return -1

        while left <= right:
            mid = (left + right) // 2
            if self.successfulQueries(mid, nums, queries):
                right = mid - 1
            else:
                left = mid + 1
        
        return left
        
    
    def successfulQueries(self, mid, nums, queries):
        difference_array = [0] * (len(nums) + 1)
        for i in range(mid):
            query = queries[i]
            difference_array[query[0]] += query[2]
            difference_array[query[1] + 1] -= query[2]
        
        prefixSum = 0
        
        for i in range(len(nums)):
            prefixSum += difference_array[i]
            if nums[i] > prefixSum:
                return False
        
        return True
        
        
