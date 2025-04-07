class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # knapsack :(
        # sum can only be sum(nums) / 2
        if sum(nums) % 2:
            return False

        target = sum(nums) // 2
        cache = {}

        # row is sum thus far
        # col is index in nums
        dp = [[0 for _ in range(len(nums) + 1)] for _ in range(target + 1)]
        
        for maxW in range(1, len(dp)):
            for idx in range(1, len(dp[0])):
                leaveRes = dp[maxW][idx - 1]
                if nums[idx - 1] <= maxW:
                    dp[maxW][idx] = max(nums[idx - 1] + dp[maxW - nums[idx - 1]][idx - 1], leaveRes)
                else:
                    dp[maxW][idx] = leaveRes
        
        # for i in range(len(dp)):
        #     print(i, dp[i])

        return dp[-1][-1] == target
