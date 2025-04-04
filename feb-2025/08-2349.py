class NumberContainers:

    def __init__(self):
        self.numbers = defaultdict(set)
        self.numbersOrdered = defaultdict(list)
        self.containers = defaultdict(int)

    def change(self, index: int, number: int) -> None:
        if index in self.containers:
            oldNum = self.containers[index]
            self.numbers[oldNum].discard(index)
        self.containers[index] = number
        self.numbers[number].add(index)
        heappush(self.numbersOrdered[number], index)
        # print(self.numbersOrdered)
        # print(self.numbers, self.containers)

    def find(self, number: int) -> int:
        # print("find " + str(number))
        # print(self.numbers[number])
        if self.numbers[number]:
            # print(self.numbersOrdered[0], self.numbers[number])
            while self.numbersOrdered[number][0] not in self.numbers[number]:
                heappop(self.numbersOrdered[number])
            return self.numbersOrdered[number][0]
        return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)