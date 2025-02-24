class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        nodes = {}

        # construct adjacency list
        for edge in edges:
            if edge[0] in nodes:
                nodes[edge[0]][1].append(edge[1])
            else:
                nodes[edge[0]] = [10001, [edge[1]]]
            if edge[1] in nodes:
                nodes[edge[1]][1].append(edge[0])
            else:
                nodes[edge[1]] = [10001, [edge[0]]]

        def traverseBob(curr, prev, turn, path):
            path.append(curr)
            
            # reached 0
            if curr == 0:
                return path, True
            
            # reached leaf that isn't 0
            if len(nodes[curr][1]) == 1 and turn != 0:
                path.pop()
                return [], False

            # shortest = None
            
            # at a junction
            for nextNode in nodes[curr][1]:
                if nextNode != prev:
                    newPath, success = traverseBob(nextNode, curr, turn + 1, path)
                    if success:
                        return newPath, True
            
            # none of the paths from this node was correct
            path.pop()
            return [], False
        
        bobPath, success = traverseBob(bob, -1, 0, [])

        for i in range(len(bobPath)):
            nodes[bobPath[i]][0] = i

        aliceSeen = set([0])

        def traverseAlice(curr, prev, turn, profit):
            if turn < nodes[curr][0]:
                profit += amount[curr]
            elif turn == nodes[curr][0]:
                profit += amount[curr] / 2
            
            # reached leaf
            if len(nodes[curr][1]) == 1 and turn != 0:
                return profit
            
            maxProfit = None

            for nextNode in nodes[curr][1]:
                if nextNode != prev:
                    aliceSeen.add(nextNode)
                    subtreeAmt = traverseAlice(nextNode, curr, turn + 1, profit)
                    if maxProfit == None or subtreeAmt > maxProfit:
                        maxProfit = subtreeAmt
            
            return maxProfit
        
        

        return int(traverseAlice(0, -1, 0, 0))
