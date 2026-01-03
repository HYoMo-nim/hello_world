# [1] 

a=[0]*43

for i in range(10):
    b=int(input())
    b=b%42
    a[b]+=1


cnt = 0

for i in range(0, 43):
    if(a[i]!=0):
        cnt+=1

print(cnt)

# [2] 

a=int(input())
b=int(input())
c=int(input())

d=str(a*b*c)
cnt = [0]*10 #여기도 

for i in d: # 각 자리를 카운팅
    for j in range(10): #오답! 숫자 자리는 0~9로 총 10개임
        if int(i)==j:
            cnt[j]+=1
            break
            
for i in cnt:
    print(i)

#[3] 8958 OX 퀴즈 

a=int(input())

# 연속된 0 개수를 저장할 변수
# 총 점수를 저장할 변수

for i in range(a):
    b=input()
    seq=0
    total=0

    for j in range(len(b)):
        
        if b[j]=='X':
            seq=0
            continue

        if b[j]=='O':
            seq+=1
            total+=seq
        

    print(total)

        
# [4] 1978 소수 찾기 

n=int(input())
a=list(map(int,input().split()))
cnt=0

for i in a:
    for j in range(2,i+1):
        if i%j ==0:
            if i==j:
                cnt+=1
            break

print(cnt)

# [5] 수 정렬하기 

n = int(input())
a=[0]*n

for i in range(n):
    a[i]=int(input())

a.sort()

for i in range(n):
    print(a[i])


# [6] 블랙잭

n,m=map(int,input().split())
a=list(map(int,input().split()))

total=0

for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if (a[i]+a[j]+a[k]) > m:
                continue
            else:
                total=max(total,a[i]+a[j]+a[k])
print(total)

# [7] 벌집 

# 방 개수 1->6(2-7)->12(8-19)->18()

n=int(input())

num=1
cnt=1

while(n>num):
    num+=6*cnt
    cnt+=1

print(cnt) 