class Solution:
    def punishmentNumber(self, n: int) -> int:

        def partit_sum(num, target, currSum):
            if currSum > target:
                return False
            if currSum + num == target:
                return True
            num_str = str(num)
            for j in range(1, len(num_str)):
                this_partit = int(num_str[j :])
                next_partit = int(num_str[: j])
                if partit_sum(next_partit, target, currSum + this_partit):
                    return True
            
            return False
        
        punishment_num = 0

        for i in range(1, n + 1):
            square = i * i
            print(i)
            if partit_sum(square, i, 0):
                punishment_num += square
        
        return punishment_num