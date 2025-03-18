class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        usedBits = 0
        left = 0
        res = 0

        for right in range(len(nums)):
            while usedBits & nums[right] != 0:
                usedBits ^= nums[left]
                left += 1
            
            usedBits |= nums[right]
            res = max(res, right - left + 1)
        
        return res
