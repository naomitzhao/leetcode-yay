class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        products = {}
        res = 0

        for i in range(len(nums)):
            for j in range(len(nums)):
                if j == i:
                    continue
                product = nums[i] * nums[j]
                if product in products:
                    for k in range(len(products[product])):
                        first, second = products[product][k]
                        if first != i and first != j and second != i and second != j:
                            res += 1
                    products[product].append((i, j))
                else:
                    products[product] = [(i, j)]
        
        # print(products)
        
        return res * 2
                