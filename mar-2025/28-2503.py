class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        sortedQueries = []

        for i in range(len(queries)):
            sortedQueries.append((queries[i], i))
        
        sortedQueries.sort()
        
        q = [(grid[0][0], 0, 0)]
        visited = set([(0, 0)])
        offsets = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        pts = 0
        i = 0
        res = [0] * len(queries)
        
        for value, idx in sortedQueries:
            while q and q[0][0] < value:
                cellVal, row, col = heappop(q)
                pts += 1

                for rowOffset, colOffset in offsets:
                    newRow, newCol = (row + rowOffset, col + colOffset)
                
                    if newRow >= 0 and newRow < len(grid) and newCol >= 0 and newCol < len(grid[0]) and (newRow, newCol) not in visited:
                        heappush(q, (grid[newRow][newCol], newRow, newCol))
                        visited.add((newRow, newCol))
                
            res[idx] = pts
        
        return res
        
            