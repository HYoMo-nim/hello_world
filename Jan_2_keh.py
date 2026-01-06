# No. 10811 바구니 뒤집기
n, m=map(int, input().split())
result=""
arr=[i+1 for i in range(n)]

for i in range(m):
    start, end=map(int, input().split())
    st=0
    if start==end: continue
    else:
        arr[start-1:end]=reversed(arr[start-1:end])
        # start-1부터 end까지 기존 배열을 역순으로 뒤집어서 정렬

for i in range(n):
    result+=str(arr[i])+" "
print(result)


# No. 2587 대표값2
mid=[]

for i in range(5):
    mid.append(int(input()))

mid.sort()
print(sum(mid)//5)
print(mid[2])


# No.2745 진법 변환
B, n=map(str, input().split())

print(int(B, int(n)))


# No. 2747 피보나치 수
n=int(input())
arr=[0 for i in range(n+1)]

for i in range(n+1):
    if i==0 or i==1:
        arr[i]=i
    else:
        arr[i]=arr[i-1]+arr[i-2]

print(arr[n])


# No. 25305 커트라인
N, k=map(int, input().split())
arr=input().split()

arr=list(map(int, arr))
arr.sort(reverse=True)
print(arr[k-1])


# No. 5585 거스름돈
a=int(input())

money=1000-a
count=0

while money!=0:
    if money >=500:
        count+=1
        money-=500
    elif money>=100 and money<500:
        count+=1
        money-=100
    elif money>=50 and money<100:
        count+=1
        money-=50
    elif money>=10 and money<50:
        count+=1
        money-=10
    elif money>=5 and money<10:
        count+=1
        money-=5
    else:
        count+=1
        money-=1

print(count)


# No. 19532 수학은 비대면 강의입니다
a, b, c, d, e, f=map(int, input().split())

y=(a*f-c*d)//(a*e-b*d)
x=(b*f-c*e)//(b*d-a*e)

result=str(x)+" "+str(y)

print(result)




