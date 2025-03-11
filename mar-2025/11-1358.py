class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # maintain sliding window with minimum containing abc
        # the number of substrings that window gets is based on position of start

        letters = set(['a', 'b', 'c'])
        left = 0
        freqs = {}
        count = 0
        for right in range(len(s)):
            if s[right] in letters:
                if s[right] in freqs:
                    freqs[s[right]] += 1
                else:
                    freqs[s[right]] = 1
            
            while s[left] not in freqs or s[left] in freqs and freqs[s[left]] > 1:
                if s[left] in freqs:
                    freqs[s[left]] -= 1
                left += 1
            
            if len(freqs) == 3:
                count += left + 1
        
        return count

