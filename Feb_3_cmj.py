# No. 1065  한수------------------------------------------------
n = int(input())
count = 0
for i in range(1, n + 1):
    if i < 100:
        count += 1
    else:
        s = str(i)
        if int(s[0]) - int(s[1]) == int(s[1]) - int(s[2]):
            count += 1
print(count)

# No. 10773  제로------------------------------------------------
k = int(input())
stack = []
for _ in range(k):
    num = int(input())
    if num == 0:
        stack.pop()
    else:
        stack.append(num)
print(sum(stack))

# No. 2164    카드2------------------------------------------------
n = int(input())
from collections import deque
queue = deque(range(1, n + 1))
while len(queue) > 1:
    queue.popleft()
    queue.append(queue.popleft())
print(queue[0])
