class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        # make frequency map of all values subtracted by their index
        # [4, 1, 3, 3] -> [4, 0, 1, 0]
        # [5, 7, 7, 9] -> [5, 6, 5, 6]
        #   good pairs have the same value.

        n = len(nums)

        values = defaultdict(int) 
        goodPairs = 0

        for i in range(n):
            goodPairs += values[nums[i] - i]
            values[nums[i] - i] += 1
        
        # total number of pairs: n C 2 = n! / 2(n - 2)! = n(n-1) / 2
        return int(n * (n-1) / 2 - goodPairs)
