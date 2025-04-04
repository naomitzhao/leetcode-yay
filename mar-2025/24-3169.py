class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        maxDay = meetings[0][1]

        daysAvail = meetings[0][0] - 1
        for i in range(1, len(meetings)):
            if meetings[i][1] > maxDay:
                daysAvail += max(0, meetings[i][0] - maxDay - 1)
            maxDay = max(maxDay, meetings[i][1])
        
        daysAvail += days - maxDay
        
        return daysAvail