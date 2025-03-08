class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # sliding window
        numWhite = 0
        minWhite = 100
        left = 0
        for right in range(len(blocks)):
            if blocks[right] == 'W':
                numWhite += 1
            if right - left + 1 == k:
                minWhite = min(minWhite, numWhite)
                if blocks[left] == 'W':
                    numWhite -= 1
                left += 1
        
        return minWhite

