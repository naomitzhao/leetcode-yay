class ProductOfNumbers:

    def __init__(self):
        self.products = [1]  # prefix product
        self.zeros = []

    def add(self, num: int) -> None:
        if num == 0:
            self.zeros.append(len(self.products))
        if self.products[-1] == 0:
            self.products.append(num)
        else:
            self.products.append(self.products[-1] * num)

    def getProduct(self, k: int) -> int:
        start_idx = len(self.products) - k - 1

        for zero_idx in self.zeros:
            if zero_idx > start_idx:
                return 0

        start_val = self.products[start_idx]

        if start_val == 0:
            start_val = 1

        return int(self.products[-1] / start_val)

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
