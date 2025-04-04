class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        valuesNeeded = set([i for i in range(1, len(grid) * len(grid) + 1)])

        a = None
        b = None

        for row in range(len(grid)):
            for col in range(len(grid)):
                value = grid[row][col]
                if value in valuesNeeded:
                    valuesNeeded.remove(value)
                else:
                    a = value
        
        b = list(valuesNeeded)[0]
        return [a, b]
