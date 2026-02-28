# 1065  한수

a=int(input())
cnt=0

for i in range(1,a+1):
    
    num_list = list(map(int, str(i)))

    if i < 100:
        cnt += 1  
    elif num_list[0]-num_list[1] == num_list[1]-num_list[2]:
        cnt += 1  

print(cnt)

# 10773

import sys

K = int(sys.stdin.readline())    

ST = []                   

for _ in range(K):  
    n = int(sys.stdin.readline())  

    if ST and n == 0: 
        ST.pop()        
    else:
        ST.append(n)  

print(sum(ST))         

# 2164 카드2(시간복잡도 빠름)

n = int(input())
square = 2

while True:
    if (n == 1 or n == 2):
        print(n)
        break

    square *= 2

    if (square >= n):
        print((n - (square // 2)) * 2)
        break

# 2164 카드2(2)

from collections import deque

n = int(input())
card = deque(range(1, n+1)) # 1부터 n까지 숫자를 생성

while len(card) > 1:
    card.popleft()        # 맨 위 카드 버림
    card.append(card.popleft())  # 다음 카드 맨 뒤로 이동

print(card[0])