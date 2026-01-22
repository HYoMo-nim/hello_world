# 11650 좌표
'''
n=int(input())
a=[]

for i in range(n):
    x,y=map(int,input().split())
    a.append((x,y))

a.sort()

for i in a:
    print(*i) #*는 언패킹 연산자'''

# 10814 나이순 정렬
'''
n=int(input())
b=[]
for i in range(n):
    a=input().split()
    a[0]=int(a[0])
    b.append((a[0],a[1]))

b.sort(key=lambda x: x[0])
# key: 이 기준에 맞춰서 정렬할 것, 함수가 들어가야 함(이 함수를 적용해 정렬)
# lambda x: x[0]: 익명 함수(이름 없는 함수) 
# lambda: 지금부터 함수를 만들겠다는 선언, x: 매개변수(리스트 b의 요소가 x에 하나씩 대입), x[0]: 튜플의 0번째 요소를 반환한드ㅏ는 뜻

for i in b:
    print(*i)'''


# 4673 셀프넘버
'''
arr=list(range(1,10001))

for i in range(1,10001):
    for j in str(i):
        i+=int(j)
    if i in arr:
        arr.remove(i)

for i in arr:
    print(i)'''


# 1427 소트인사이드
'''
import sys

n=sys.stdin.readline().strip() #속도 
n_list=list(n)
n_list.sort(reverse=True)
print(*n_list,sep='')'''


# 1010 다리놓기
'''import sys
import math

t=int(input())
for _ in range(t):
    a,b=map(int,sys.stdin.readline().split())
    result=math.comb(b,a) #큰 수가 앞에 와야 함(ex: a=3 b=5일 경우, 3개 중 5개를 뽑는 방법은 없으므로 0을 반환)
    print(result)'''

# 10815 숫자 카드
'''import sys
input=sys.stdin.readline

n=int(input())
a=set(map(int,input().split())) #중복 제거
m=int(input())
b=list(map(int,input().split()))

for i in b:
    if i in a:
        print(1, end=" ")
    else:
        print(0, end=" ") 
'''

# 1436 영화감독 숌

n=int(input())
a=666
cnt=0

while True:
    if '666' in str(a):
        cnt+=1
    
    if cnt==n:
        break

    a+=1

print(a)


# 이거진짜독특하네 vsCode에선 안돌아가는데 백준에선 맞았대