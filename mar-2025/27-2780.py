class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        forward = []
        freqs = {}
        mostFreq = [None, 0]

        for i in range(len(nums)):
            if nums[i] in freqs:
                freqs[nums[i]] +=1
            else:
                freqs[nums[i]] = 1
            
            if freqs[nums[i]] > mostFreq[1]:
                mostFreq = [nums[i], freqs[nums[i]]]
            
            if mostFreq[1] > (i + 1) / 2:
                forward.append(mostFreq[0])
            else:
                forward.append(-1)
        
        backFreqs = {}
        backward = [-1] * len(nums)
        mostFreq = [None, 0]
        
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] in backFreqs:
                backFreqs[nums[i]] += 1
            else:
                backFreqs[nums[i]] = 1
            
            if backFreqs[nums[i]] > mostFreq[1]:
                mostFreq = [nums[i], backFreqs[nums[i]]]
        
            if mostFreq[1] > (len(nums) - i) / 2:
                backward[i] = mostFreq[0]
            else:
                backward[i] = -1
        
        # print(forward)
        # print(backward)
        
        for i in range(len(forward) - 1):
            if forward[i] != -1 and forward[i] == backward[i + 1]:
                return i
        
        return -1
        
