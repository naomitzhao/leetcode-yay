class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        # convert n so each digit is less than limit
        def normalize(n):
            res = 0
            n_string = str(n)
            currently_less = False
            for digit in n_string:
                digit_num = int(digit)
                if currently_less:
                    res = res * 10 + limit
                elif digit_num > limit:
                    currently_less = True
                    res = res * 10 + limit
                else:
                    res = res * 10 + digit_num
            return res
        
        # how many prefixes possible in (limit + 1)-ary world
        def count(n):
            res = 0
            base = limit + 1
            prefix = str(n)[:-len(s)]

            for digit in prefix:
                res = res * base + int(digit)
            
            if int(prefix + s) <= n:
                res += 1

            return res
        
        return count(normalize(finish)) - count(normalize(start - 1))
