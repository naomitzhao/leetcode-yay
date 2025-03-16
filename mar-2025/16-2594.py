class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        ranks.sort()
        self.ranks = ranks
        self.cars = cars

        left = 1
        right = cars * cars * max(ranks)

        while left < right:
            mid = (left + right) // 2
            if self.underPossible(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
        
    
    def underPossible(self, limitEach):
        repaired = 0
        for i in range(len(self.ranks)):
            rank = self.ranks[i]
            thisRepaired = int(math.sqrt(limitEach // rank))
            repaired += thisRepaired
        
        if repaired >= self.cars:
            return True
        
        return False

