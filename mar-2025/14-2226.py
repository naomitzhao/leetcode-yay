class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0
        left = 1
        right = max(candies)
        lastValid = 0
        while left <= right:
            mid = (left + right) // 2
            allocatable = True
            fed = 0
            for candyPile in candies:
                fed += candyPile // mid
            if fed >= k:
                lastValid = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return lastValid
