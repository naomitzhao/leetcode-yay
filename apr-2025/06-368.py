class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # dp: store length, smallest, largest
        # dp = [[-1 for _ in range(len(nums))] for _ in range(len(nums))]

        nums.sort()

        # go backwards until you get to one you're divisible by
        # choose the one that's longer
        best = (1, [nums[0]])
        dp = [(1, [nums[0]])]
        for i in range(1, len(nums)):
            longest = (1, [nums[i]])
            for j in range(0, i):
                if nums[i] % nums[j] == 0 and dp[j][0] + 1 > longest[0]:
                    longest = (dp[j][0] + 1, dp[j][1] + [nums[i]])
            dp.append(longest)
            if longest[0] > best[0]:
                best = longest
        
        # for i in range(len(nums)):
        #     print(i, nums[i], dp[i])

        return best[1]
