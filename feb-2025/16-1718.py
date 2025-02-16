class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        if n == 1:
            return [1]
        
        res = [0] * (n * 2 - 1)
        res[0] = n
        res[n] = n

        not_done = set([i for i in range(1, n)])

        def construct(idx: int, curr):

            if not not_done or idx >= len(res):
                return curr, True

            if curr[idx]:
                return construct(idx + 1, curr) 
                
            ret_success = False
            best_try = curr[:]

            for num in reversed(sorted(list(not_done))):
                if ret_success:
                    break
                special_cond = True
                next_idx = idx + num
                if num != 1 and (next_idx >= len(curr) or curr[next_idx]):
                    special_cond = False
                
                if special_cond:
                    if num != 1:
                        curr[next_idx] = num
                    curr[idx] = num
                    not_done.discard(num)
                    nxt, success = construct(idx + 1, curr)
                    if success:
                        best_try = nxt[:]
                        ret_success = True
                    curr[idx] = 0
                    if num != 1:
                        curr[next_idx] = 0
                    not_done.add(num)
            
            return best_try, ret_success
        
        best_try, success = construct(1, res)
        return best_try

