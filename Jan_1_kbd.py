#[2]1월 1주차 (12/28~1/3)
#5622 다이얼 
#방 개수 1->6(2-7)->12(8-19)->18()

'''n=int(input())

num=1
cnt=1

while(n>num):
    num+=6*cnt
    cnt+=1

print(cnt)'''

# 2231 분해합 

'''n= int(input())

for i in range(1, n+1):
    num=sum((map(int,str(i))))
    num_sum=i+num
    
    if num_sum==n: 
        print(i)
        break

    if i==n:
        print(0)'''

# 15596 정수 N개의 합

'''def solve(a):
    return sum(a)'''

# 2920 음계

'''a=list(map(int,input().split()))

for i in range(8):
    if i==7:
        print("ascending")
        exit()
    if a[i]!=a[i+1]-1:
        break


for i in range(8):
    if i==7:
        print("descending")
        exit()
    if a[i]!=a[i+1]+1:
        break

print("mixed")'''

# 2581 소수

'''m=int(input())
n=int(input())
arr=[]
sum_=0

for i in range(m,n+1):

    if i<2: #1은 소수가 아니므로 제외
        continue 

    is_prime=True
    for j in range (2, i):
        if i%j==0:
            is_prime=False
            break

    if is_prime:
        arr.append(i)

if arr: #arr이 비어 있지 않나?
    print(sum(arr))
    print(min(arr))

else:
    print(-1)'''

# 10813 공 바꾸기

'''a,b=map(int,input().split())
arr=[]

for i in range(a):
    arr.append(i+1)

# arr[i]+=i+1이 더 빠름

for i in range(b):
    d,e=map(int,input().split())
    temp=arr[d-1]
    arr[d-1]=arr[e-1]
    arr[e-1]=temp

print(' '.join(map(str,arr)))'''

# 1712 손익 분기점

'''a,b,c=map(int,input().split())

if b>=c:
    print(-1)
    # 손익 분기점을 넘지 못하는 경우임

else: 
    print(int(a//(c-b)+1))'''