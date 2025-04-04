class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        mp = defaultdict(list)
        MOD = 10 ** 9 + 7
        for road in roads:
            mp[road[0]].append((road[1], road[2]))
            mp[road[1]].append((road[0], road[2]))
        
        # dijkstra
        q = [(0, 0)]
        shortestTimes = {}
        for i in range(n):
            shortestTimes[i] = [float('inf'), 1]

        while q:
            currTime, currNode = heappop(q)
            if currTime > shortestTimes[currNode][0]:
                continue
            
            for nextNode, nextTime in mp[currNode]:
                if currTime + nextTime < shortestTimes[nextNode][0]:
                    shortestTimes[nextNode] = [currTime + nextTime, shortestTimes[currNode][1] % MOD]
                    heappush(q, (shortestTimes[nextNode][0], nextNode))
                elif currTime + nextTime == shortestTimes[nextNode][0]:
                    shortestTimes[nextNode][1] = (shortestTimes[nextNode][1] + shortestTimes[currNode][1]) % MOD

        return shortestTimes[n - 1][1]