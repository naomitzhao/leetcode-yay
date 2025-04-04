class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        i = 0
        res = []
        zeros = 0
        while i < len(nums):
            if i == len(nums) - 1:
                res.append(nums[i])
            elif nums[i] == 0:
                zeros += 1
            elif nums[i] == nums[i + 1]:
                res.append(nums[i] * 2)
                zeros += 1
                i += 1
            else:
                res.append(nums[i])
            i += 1
        
        for i in range(zeros):
            res.append(0)
        
        return res
