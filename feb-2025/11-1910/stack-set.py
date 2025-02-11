# not very straightforward solution i made initially 
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        new_string = []
        in_row = []
        
        for i in range(len(s)):
            new_string.append(s[i])
            next_set = set([0])
            if s[i] == part[0]:
                next_set.add(1)
            if in_row:
                for last_idx in in_row[-1]:
                    if s[i] == part[last_idx]:
                        next_set.add(last_idx + 1)
                    
            in_row.append(next_set)

            if in_row and len(part) in in_row[-1]:
                for j in range(len(part)):
                    new_string.pop()
                    in_row.pop()
            
        
        return ''.join(new_string)
            
