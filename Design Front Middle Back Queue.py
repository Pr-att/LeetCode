class FrontMiddleBackQueue:

    def __init__(self):
        self.array = []
        

    def pushFront(self, val: int) -> None:
        self.array.insert(0, val)

    def pushMiddle(self, val: int) -> None:
        self.array.insert(len(self.array) // 2, val)
        

    def pushBack(self, val: int) -> None:
        print(self.array)
        self.array.append(val)

    def popFront(self) -> int:
        print(self.array)
        if not self.array:
            return -1
        return self.array.pop(0)

    def popMiddle(self) -> int:
        print(self.array)
        if not self.array:
            return -1
        if len(self.array) % 2 == 0:
            return self.array.pop((len(self.array) // 2) - 1)
        else:
            return self.array.pop(len(self.array) // 2)

    def popBack(self) -> int:
        print(self.array)
        if not self.array:
            return -1
        return self.array.pop()
        


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()