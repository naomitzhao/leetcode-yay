class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        balls = {}
        colors = {}
        colorTracker = []

        for query in queries:
            if query[0] in balls:
                oldColor = balls[query[0]]
            else:
                oldColor = 0
            newColor = query[1]
            if newColor in colors:
                colors[newColor] += 1
            else:
                colors[newColor] = 1

            balls[query[0]] = newColor
            
            if oldColor in colors:
                if colors[oldColor] == 1:
                    del colors[oldColor]
                else:
                    colors[oldColor] -= 1
            
            colorTracker.append(len(colors))

        return colorTracker