class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        # count k-palindromic integers
        good_integers = 0

        # save digit combinations we've seen
        seen = set()
        
        # pre compute factorial values
        fac = [factorial(i) for i in range(n + 1)]

        base = 10 ** ((n - 1) // 2)

        skip = n & 1

        for firstHalf in range(base, base * 10):
            s = str(firstHalf)
            
            s += s[::-1][skip:]
            i = int(s)
            numStr = str(i)

            if i % k:
                continue
            
            sortDigits = ''.join(sorted(numStr))
            if sortDigits in seen:
                continue
            seen.add(sortDigits)
            perms = -1

            freqs = [0] * 10
            for j in range(len(numStr)):
                digit = numStr[j]
                freqs[int(digit)] += 1

            perms = (n - freqs[0]) * fac[n - 1]
            for j in range(10):
                perms //= fac[freqs[j]]
            
            good_integers += perms
        
        return good_integers
