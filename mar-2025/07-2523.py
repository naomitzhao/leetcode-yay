class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def isPrime(num):
            if num == 1:
                return False
            for i in range(2, int(sqrt(num) + 1)):
                if num % i == 0:
                    return False
            
            return True
        
        prime1 = None
        prime2 = None
        lastPrime = None

        for i in range(left, right + 1):
            if isPrime(i):
                if not prime1:
                    prime1 = i
                elif not prime2:
                    prime2 = i
                else:
                    if i - lastPrime < prime2 - prime1:
                        prime1 = lastPrime
                        prime2 = i
                lastPrime = i
                if prime2 and prime2 - prime1 == 2:
                    break
        
        if not prime2:
            return [-1, -1]
        
        return [prime1, prime2]
