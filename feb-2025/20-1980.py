class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        seen = set(nums)

        m = len(nums)
        n = len(nums[0])
        
        def getUnseen(currList):
            if len(currList) == n:
                if ''.join(currList) in seen:
                    return None
                return ''.join(currList)
            
            currList.append('0')
            zeroRes = getUnseen(currList)
            if zeroRes:
                return zeroRes
            currList.pop()

            currList.append('1')
            oneRes = getUnseen(currList)
            if oneRes:
                return oneRes
            currList.pop()
            
            return None
        
        return getUnseen([])
