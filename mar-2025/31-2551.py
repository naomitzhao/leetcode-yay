class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        # k bags -> k + 1 weights will be chosen
        # need at least one pair
        # 
        weightHeap = []

        # min score: min heap
        for i in range(len(weights) - 1):
            heappush(weightHeap, weights[i] + weights[i + 1])

        minScore = weights[0] + weights[-1]
        smallestIdx = None
        largestIdx = None
        for i in range(k - 1):
            nextSmallest = heappop(weightHeap)
            # print(nextSmallest)
            minScore += nextSmallest
        
        weightHeap = []
        # max score: max heap
        for i in range(len(weights) - 1):
            heappush(weightHeap, -weights[i] - weights[i + 1])
        maxScore = weights[0] + weights[-1]
        # print("max")
        for i in range(k - 1):
            nextLargest = heappop(weightHeap)
            # print(nextLargest)
            maxScore -= nextLargest
        
        return maxScore - minScore