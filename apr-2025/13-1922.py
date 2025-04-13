class Solution:
    def countGoodNumbers(self, n: int) -> int:
        # combinatorics
        # even digits have 5 choices, odd digits have 4 choices
        # for length n, there are (n + 1) // 2 even numbers and n // 2 odd numbers
        MOD = 10 ** 9 + 7

        # binary exponentiation
        def binPower(a, b):
            if b == 0:
                return 1
            res = binPower(a, b // 2)
            if b % 2:
                return res * res * a % MOD
            else:
                return res * res % MOD

        return (binPower(5, (n + 1) // 2) * binPower(4, n // 2)) % MOD
