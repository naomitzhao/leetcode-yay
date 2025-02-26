class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        # prefix sum
        prefixes = [0]
        minToNow = 0
        maxToNow = 0
        maxSum = 0

        for num in nums:
            nextPrefix = prefixes[-1] + num
            prefixes.append(nextPrefix)
            minToNow = min(minToNow, nextPrefix)
            maxToNow = max(maxToNow, nextPrefix)
            maxSum = max(maxSum, max(abs(nextPrefix - minToNow), abs(nextPrefix - maxToNow)))
        
        return maxSum
