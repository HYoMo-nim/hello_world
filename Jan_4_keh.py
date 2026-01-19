
# No. 11650 좌표 정렬하기
'''
예전에 작성했던 코드
a=int(input())
arr=[]

for i in range(a):
    x, y=map(int, input().split())
    arr.append([x, y]) # arr 리스트에 x(리스트) 추가

arr.sort()

for i in range(a):
    print(arr[i][0], arr[i][1])
'''

a=int(input())
arr=[]

for i in range(a):
    x, y=map(int, input().split())
    arr.append([x, y])

result=sorted(arr, key=lambda x: (x[0], x[1]))

for x, y in result:
    print(x, y)
    
# lambda에 대해선: https://seonybob3210.tistory.com/17


#No. 10814 나이순 정렬
n=int(input())
arr=[]

for i in range(n):
    x, y=map(str, input().split())
    arr.append([int(x), y])

result=sorted(arr, key=lambda x:(x[0]))

for x, y in result:
    print(x, y)


#No. 4673 셀프 넘버
result=[0 for i in range(10000)]

for i in range(10000):
    if i<10:
        a=i+i
        result[int(a)]+=1
    elif i<100 and i>=10:
        a=i+i//10+i%10
        result[int(a)]+=1
    elif i<1000 and i>=100:
        a=i+i//100+(i%100)//10+(i%10)
        result[int(a)]+=1
    else:
        a=i+i//1000+(i%1000)//100+(i%100)//10+(i%10)
        if a<10000:
            result[int(a)]+=1
        
for i in range(10000):
    if result[i]==0:
        print(i)
    else:
        continue
        
# '/'연산자는 소수점까지 출력함.
# 위의 코드같은 경우 result에 넣을 때 a를 int로 변환하기 때문에 더하는 과정 중 소수점이 섞여들어가 오류 발생
# 따라서 정수나눗셈을 하는 '//' 연산자로 계산해야 함.


#No. 1427 소트인사이드
r=input()
arr=[0 for i in range(len(r))]
for i in range(len(r)):
    arr[i]=int(r[i])

arr.sort(reverse=True)
for i in range(len(arr)):
    print(arr[i], end="")


#No. 1010 다리 놓기
def fact(n):
    if(n>1): return n*fact(n-1)
    else: return 1

n=int(input())

for i in range(n):
    x, y=map(int, input().split())
    result=1

    if x==1: result=y
    elif x>y: result=fact(x)//(fact(y)*fact(x-y))
    else: result=fact(y)//(fact(x)*fact(y-x))

    print(result)


#No. 10815 숫자 카드
N=int(input())
arr1=list(map(int, input().split(" ")))
M=int(input())
arr2=list(map(int, input().split(" ")))

result={}

for i in range(N):
    result[arr1[i]]=0

for i in range(M):
    if arr2[i] in result:
        print(1, end=" ")
    else:
        print(0, end=" ")
        
# 시간초과 문제 때문에 시간복잡도 O(1)인 딕셔너리 사용

        
#No. 1436 영화감독 숌
N=int(input())
num=1

while N!=0:
    num+=1
    if str(num).find("666")!=-1:
        N-=1

print(num)

