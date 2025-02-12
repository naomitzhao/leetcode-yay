class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def sumDigits(num):
            res = 0
            while num:
                res += num % 10
                num = num // 10
            return res

        possibleSums = {}  # key: possible sum, value: tuple of idxs with max elements
        maxSum = -1

        for i in range(len(nums)):
            sumRes = sumDigits(nums[i])
            if sumRes in possibleSums:
                if possibleSums[sumRes][1] == -1:
                    possibleSums[sumRes][1] = nums[i]
                else:
                    if possibleSums[sumRes][1] <= possibleSums[sumRes][0] and possibleSums[sumRes][1] < nums[i]:
                        possibleSums[sumRes][1] = nums[i]
                    elif possibleSums[sumRes][0] < possibleSums[sumRes][1] and possibleSums[sumRes][0] < nums[i]:
                        possibleSums[sumRes][0] = nums[i]

                maxSum = max(maxSum, possibleSums[sumRes][0] + possibleSums[sumRes][1])
            else:
                possibleSums[sumRes] = [nums[i], -1]
        
        return maxSum
                
                
                