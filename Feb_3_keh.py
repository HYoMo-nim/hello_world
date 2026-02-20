# No. 1065 한수 ---------------------------
a=int(input())
count=0

for i in range(1, a+1):
    if i<100:
        count+=1
    if i>=100 and i<1000:
        x=i//100
        y=(i%100)//10
        z=i%10
        if y-x==z-y:
            count+=1

print(count)


# No. 10773 제로 ---------------------------
a=int(input())
stack=[]

for i in range(a):
    b=int(input())
    if b==0:
        stack.pop()
    else:
        stack.append(b)

sum=0
for i in stack:
    sum+=i
    
print(sum)


# No. 2164 카드2 ---------------------------
import queue

que=queue.Queue()
n=int(input())

for i in range(n):
    que.put(i+1)

while que.qsize()!=1:
    que.get()
    a=que.get()
    que.put(a)

print(que.get())

