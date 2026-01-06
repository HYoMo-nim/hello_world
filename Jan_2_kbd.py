# 바구니 뒤집기 10811
#첫번째 줄 n,m-> 바구니 개수, 바꾸는 횟수
#m번간 바구니를 역순으로 만드는 방법 n개 제시

''' n,m=map(int,input().split())
basket=[0]*n

for i in range(n):
    basket[i]=i+1

for i in range(m):
    a,b=map(int,input().split())
    temp=basket[a-1:b]
    temp.reverse()
    basket[a-1:b]=temp

print(*basket)

# 1 2 3 4 5
# 2 1 3 4 5
# 2 1 4 3 5
# 3 4 1 2 5 

'''

#대표값2(2587)
#값 5개 받음 > 평균 중앙값 출력 


'''arr=[0]*5 #초기화하지 않으면 아랫줄에서 오류가 남 
# 파이썬 리스트는 크기가 자동으로 늘어나지 않기 때문에 바로 값을 넣으려고 하면 그 위치가 범위 밖이라는 메시지를 보냄

for i in range(5):
    arr[i]=int(input())

avg=0
arr.sort() #arr=arr.sort()가 아님
mid=arr[2]
 
# 아래처럼 하지 않고,
# print(sum(arr)//5)가 더 간단


for i in range(5):
    avg+=arr[i]


print(avg//5)
print(mid)


'''

# 진법 변환 2745번 
# 1. n과 b받기 


''' n,b=input().split()'''

# 파이썬의 int()함수는 진수 변환 가능
# 문법: int(string,base)
# string을 base 기수로 변환한다 
# print(int(n,int(b)))

'''b=int(b)
res=0

for i in range(len(n)):
    if 'A' <= n[i] <= 'Z':
        # A는 ord() 값이 65이므로 10으로 만들기 위해 -55 
        value = ord(n[i])-55
    else:
        value = int(n[i])

    res+=value*(b**(len(n)-1-i))
    
print(res)'''

# 피보나치수 2747

'''n=int(input())

a,b=0,1

for i in range(n):
    a,b=b,a+b

print(a)'''

# 커트라인 25305

'''n,k=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
print(a[n-k])'''

# 거스름돈 5585
'''
n=int(input())
n=1000-n
cnt=0
while n>0:
    if n>=500:
        n-=500
        cnt+=1
        continue
    
    if n>=100:
        n-=100
        cnt+=1
        continue

    if n>=50:
        n-=50
        cnt+=1
        continue

    if n>=10:
        n-=10
        cnt+=1
        continue

    if n>=5:
        n-=5
        cnt+=1
        continue

    if n>=1:
        n-=1
        cnt+=1
        continue

print(cnt)'''

# 수학은 비대면강의입니다 19532
'''
a,b,c,d,e,f=map(int,input().split())

print((c*e-b*f)//(a*e-b*d),(a*f-d*c)//(a*e-b*d))

'''