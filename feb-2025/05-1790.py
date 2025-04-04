class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diffs = []

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diffs.append([i, s1[i], s2[i]])
        
        # print(diffs)
        
        if len(diffs) == 0 or (len(diffs) == 2 and (diffs[0][1] == diffs[1][2] and diffs[0][2] == diffs[1][1])):
            return True

        return False 