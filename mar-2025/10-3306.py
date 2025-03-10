class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vowelFreqs = [0, 0, 0, 0, 0]
        uniqueVowels = 0
        vowels = {
            'a': 0,
            'e': 1,
            'i': 2,
            'o': 3,
            'u': 4
        }
        consonentCount = 0
        count = 0
        left = 0

        next_consonent = [-1] * len(word)
        curr_next_cons = len(word)
        for i in range(len(word) - 1, -1, -1):
            next_consonent[i] = curr_next_cons
            if word[i] not in vowels:
                curr_next_cons = i

        for right in range(len(word)):
            if word[right] in vowels:
                if vowelFreqs[vowels[word[right]]] == 0:
                    uniqueVowels += 1
                vowelFreqs[vowels[word[right]]] += 1
            else:
                consonentCount += 1

            while consonentCount > k:
                if word[left] in vowels:
                    vowelFreqs[vowels[word[left]]] -= 1
                    if vowelFreqs[vowels[word[left]]] == 0:
                        uniqueVowels -= 1
                else:
                    consonentCount -= 1
                left += 1
            
            while left < len(word) and uniqueVowels == 5 and consonentCount == k:
                count += next_consonent[right] - right
                if word[left] in vowels:
                    vowelFreqs[vowels[word[left]]] -= 1
                    if vowelFreqs[vowels[word[left]]] == 0:
                        uniqueVowels -= 1
                else:
                    consonentCount -= 1
                left += 1
        
        return count
