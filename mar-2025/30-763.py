class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastSeen = {}
        for i in range(len(s)):
            lastSeen[s[i]] = i
        
        ends = []
        for i in range(len(s)):
            ends.append(lastSeen[s[i]])
        
        right = 0
        currPartStart = 0
        res = []
        for left in range(len(s)):
            if ends[left] > right:
                right = ends[left]
            if left == right:
                res.append(right - currPartStart + 1)
                left += 1
                right += 1
                currPartStart = left
        
        return res