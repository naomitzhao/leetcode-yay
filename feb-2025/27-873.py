class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        dp = [[1] * len(arr) for _ in range(len(arr))]

        idxs = {}
        max_chain = 2

        for i in range(len(arr)):
            idxs[arr[i]] = i
            for j in range(i + 1, len(arr)):
                if arr[j] - arr[i] in idxs:
                    dp[i][j] = dp[idxs[arr[j] - arr[i]]][i] + 1
                    max_chain = max(max_chain, dp[i][j])
                else:
                    dp[i][j] = 2
        
        # for row in dp:
        #     print(row)
        
        if max_chain > 2:
            return max_chain
        
        return 0
