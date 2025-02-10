class Solution:
    def clearDigits(self, s: str) -> str:
        stck = []
        for ch in s:
            if ch.isdigit():
                if stck:
                    stck.pop()
            else:
                stck.append(ch)
        
        return ''.join(stck)