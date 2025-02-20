class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        allowedLetters = ['a', 'b', 'c']
        
        def getStrings(curr, count):
            strings = []
            if len(curr) == n:
                count += 1
                return ''.join(curr), count
            for letter in allowedLetters:
                if curr and letter == curr[-1]:
                    continue
                curr.append(letter)
                builtString, count = getStrings(curr, count)
                curr.pop()
                if count == k:
                    return builtString, count
            
            return "", count
        
        return getStrings([], 0)[0]