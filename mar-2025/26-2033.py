class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        flatGrid = []
        res = 0
        for row in grid:
            for item in row:
                flatGrid.append(item)

        flatGrid.sort()
        median = flatGrid[len(flatGrid) // 2]
        
        for i in range(len(flatGrid)):
            if flatGrid[i] % x != median % x:
                return -1
            res += abs(flatGrid[i] - median) // x

        return res
        