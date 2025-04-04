class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        freqs = defaultdict(int)

        for v in range(n):
            graph[v] = [v]

        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)

        for v in range(n):
            neighbors = tuple(sorted(graph[v]))
            freqs[neighbors] += 1  
            
        tot = 0

        for neighbors, freq in freqs.items():
            if len(neighbors) == freq:
                tot += 1
        
        return tot