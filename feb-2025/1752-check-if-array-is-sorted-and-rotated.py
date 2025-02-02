class Solution:
    def check(self, nums: List[int]) -> bool:
        decreases = 0
        for i in range(len(nums)):
            if nums[i] < nums[i - 1]:
                if decreases == 0:
                    decreases = 1
                else:
                    return False
        
        return True
