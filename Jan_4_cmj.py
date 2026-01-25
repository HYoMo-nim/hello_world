# No. 11650     좌표 정렬하기-----------------------------------

a = int(input())
points = []
for _ in range(a):
    x, y = map(int, input().split())
    points.append((x, y))
points.sort()

for point in points:
    print(point[0], point[1])
    
# No. 10814     나이순 정렬------------------------------------

n = int(input())
members = []
for _ in range(n):
    age, name = input().split()
    members.append((int(age), name))
members.sort(key=lambda x: x[0])
for member in members:
    print(member[0], member[1])
    
# No. 4673       셀프 넘버-------------------------------------

def d(n):
    return n + sum(map(int, str(n)))
self_numbers = set(range(1, 10001))
for i in range(1, 10001):
    self_numbers.discard(d(i))  
for number in sorted(self_numbers):
    print(number)
    
# No. 1427       소트인사이드-----------------------------------

n = input()
sorted_n = sorted(n, reverse=True)
print(''.join(sorted_n))

# No. 1010       다리 놓기--------------------------------------

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    if n == 0 or n == m:
        print(1)
    else:
        N = 1
        k = 1
        for i in range(n):
            N *= (m - i)
            k *= (i + 1)
        print(N // k)
        
# No. 10815     숫자 카드---------------------------------------
n = int(input())
cards = set(map(int, input().split()))
m = int(input())
queries = list(map(int, input().split()))
for query in queries:
    if query in cards:
        print(1, end=' ')
    else:
        print(0, end=' ')
        
# No. 1436       영화감독 숌------------------------------------
n = int(input())
count = 0
num = 666
while True:
    if '666' in str(num):
        count += 1
        if count == n:
            print(num)
            break
    num += 1
    