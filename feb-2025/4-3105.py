class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        currLen = 0
        maxLen = 0
        isIncreasing = False

        for i in range(len(nums)):
            if i == 0 or (isIncreasing and nums[i] > nums[i - 1]) or (not isIncreasing and nums[i] < nums[i - 1]):
                currLen += 1
            else:
                currLen = 2
                if nums[i] > nums[i - 1]:
                    isIncreasing = True
                elif nums[i] < nums[i - 1]:
                    isIncreasing = False
                else:
                    currLen = 1
            maxLen = max(maxLen, currLen)
            # print(str(currLen) + " at " + str(i))
            
        return maxLen
            