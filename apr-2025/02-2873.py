class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        # brute force??
        maxVal = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    maxVal = max(maxVal, (nums[i] - nums[j]) * nums[k])
        
        return maxVal