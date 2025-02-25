class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        # odd sum: any number of even numbers and odd number of odd numbers

        # bruh apparently it needs CONTIGUOUS subarray :skull:

        MOD = 10**9 + 7
        
        # how many odds
        odds = 0
        evens = 1
        prefix_sum = 0
        res = 0

        for i in range(len(arr)):
            prefix_sum += arr[i]
            if prefix_sum % 2 == 0: # even up until now, need to subtract odd
                res += odds
                evens += 1
            else:  # need to subtract evens
                res += evens
                odds += 1
            res %= MOD
            

        return res

