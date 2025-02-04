import random

CALL_COUNT = 1000
MAX_TIME = 1000000000

calls = ['["MyCalendar"']
for i in range(CALL_COUNT):
    calls.append(', "book"')
calls.append(']')

times = ['[[]']
for i in range(CALL_COUNT):
    start = random.randrange(0, MAX_TIME)
    end = random.randrange(start + 1, MAX_TIME)
    times.append(',[' + str(start) + ',' + str(end) + ']')
times.append(']')

print(''.join(calls))
print(''.join(times))