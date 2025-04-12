class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        # brute force
        count = 0

        for i in range(low, high + 1):
            numStr = str(i)
            if len(numStr) % 2:
                continue
            
            firstHalf = numStr[: len(numStr) // 2]
            secondHalf = numStr[len(numStr) // 2 :]
        
            # print(firstHalf, secondHalf)
            firstHalfSum = 0
            secondHalfSum = 0

            for digit in firstHalf:
                firstHalfSum += int(digit)
            for digit in secondHalf:
                secondHalfSum += int(digit)

            if firstHalfSum == secondHalfSum:
                count += 1

        return count
        
