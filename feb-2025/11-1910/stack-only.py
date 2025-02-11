# much better solution using stack only and string slicing
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        new_string = []

        for ch in s:
            new_string.append(ch)
            if len(new_string) >= len(part):
                start_try = len(new_string) - len(part)
                if ''.join(new_string[start_try : len(new_string)]) == part:
                    new_string = new_string[: start_try]
            
        return ''.join(new_string)
            
