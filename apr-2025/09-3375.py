class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # count unique integers greater than k

        larger_nums = set()
        for num in nums:
            if num > k:
                larger_nums.add(num)
            if num < k:
                return -1
        
        return len(larger_nums)
