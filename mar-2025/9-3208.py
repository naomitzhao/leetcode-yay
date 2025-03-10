class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        # sliding window
        left = 0
        alternateStart = 0
        count = 0
        for right in range(1, len(colors) + k - 1):
            rightIdx = right % len(colors)
            if colors[rightIdx] == colors[rightIdx - 1]:
                alternateStart = right
            if right - alternateStart + 1 == k:
                count += 1
                if alternateStart == left:
                    alternateStart += 1
            if right - left + 1 == k:
                left += 1

        return count
