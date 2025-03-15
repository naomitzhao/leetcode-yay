class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        left = 1
        right = max(nums)

        while left < right:
            mid = (left + right) // 2
            possible = 0

            i = 0
            while i < len(nums):
                if nums[i] <= mid:
                    possible += 1
                    i += 2
                else:
                    i += 1
            
            if possible >= k:
                right = mid
            else:
                left = mid + 1
        
        return left
        
