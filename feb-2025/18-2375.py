class Solution:
    def smallestNumber(self, pattern: str) -> str:
        res = []
        stack = []

        for idx in range(len(pattern) + 1):
            stack.append(idx + 1)

            if idx == len(pattern) or pattern[idx] == "I":
                while stack:
                    res.append(str(stack.pop()))

        return ''.join(res)