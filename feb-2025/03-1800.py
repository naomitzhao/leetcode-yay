class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        currSum = 0
        maxSum = 0
        for i in range(len(nums)):
            if i == 0 or nums[i] > nums[i - 1]:
                currSum += nums[i]
                maxSum = max(maxSum, currSum)
            else:
                currSum = nums[i]
        
        return maxSum