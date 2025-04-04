class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        largestDiff = []
        largestNum = None
        
        for num in nums:
            if largestNum == None or num > largestNum:
                largestNum = num
            
            if not largestDiff:
                largestDiff.append(0)
            else:
                if largestNum - num > largestDiff[-1]:
                    largestDiff.append(largestNum - num)
                else:
                    largestDiff.append(largestDiff[-1])
        
        bestVal = 0
        for i in range(len(nums) - 1, 0, -1):
            val = nums[i] * largestDiff[i - 1]
            bestVal = max(bestVal, val)
        
        return bestVal