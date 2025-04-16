class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        # sliding window

        right = -1
        pairs = 0
        freqs = {}
        count = 0

        for left in range(len(nums)):

            # get more pairs by expanding window right
            while pairs < k and right + 1 < len(nums):
                right += 1

                # make pairs with all existing of this numer
                if nums[right] in freqs:
                    pairs += freqs[nums[right]]
                    freqs[nums[right]] += 1

                # only instance of this number in this window
                else:
                    freqs[nums[right]] = 1
            
            # enough pairs to count this window
            if pairs >= k:
                count += len(nums) - right
            
            # unpair removed element from all pairs it's in
            freqs[nums[left]] -= 1
            pairs -= freqs[nums[left]]
        
        return count
