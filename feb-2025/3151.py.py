class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        nextOdd = True
        if nums[0] % 2:  # first is odd
            nextOdd = False
        
        for i in range(1, len(nums)):
            if nums[i] % 2:
                if not nextOdd:
                    return False
            else:
                if nextOdd:
                    return False
            nextOdd = not nextOdd
        
        return True
