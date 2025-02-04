class MyCalendar(object):

    def __init__(self):
        self.blocks = []

    def book(self, startTime, endTime):
        """
        :type startTime: int
        :type endTime: int
        :rtype: bool
        """
        for block in self.blocks:
            if startTime < block[1] and endTime > block[0]:
                return False
        
        self.blocks.append((startTime, endTime))
        return True

            
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)