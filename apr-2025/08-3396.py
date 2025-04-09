class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        earliestIdx = len(nums)
        seen = set()
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] in seen:
                break
            earliestIdx = i
            seen.add(nums[i])
        
        return ceil(earliestIdx / 3)
