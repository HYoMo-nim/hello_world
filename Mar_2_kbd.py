#1475 방번호

'''

import sys
input=sys.stdin.readline().strip

n=input()
cnt=[0]*10

for i in range(len(n)):

    num=int(n[i])
    
    if num==6 or num==9:
        if cnt[6]>cnt[9]:
            cnt[9]+=1

        else:
            cnt[6]+=1

    else:
        cnt[num]+=1

print(max(cnt))

'''

# 1764 듣보잡
'''
n,m=map(int,input().split())

arr1=set()
for i in range(n):
    arr1.add(input()) #set은 add로 추가

arr2=set()
for i in range(m):
    arr2.add(input())

result=sorted(list(arr1&arr2)) # 교집합. 합집합은 a1|a2, 차집합은 a1-a2

print(len(result))

print('\n'.join(result))

'''

# 11866 요세푸스 문제 0

n,k=map(int,input().split())

arr=[i for i in range(1,n+1)]

result=[]
idx=0

for i in range(n):
    idx=(idx+k-1)%len(arr)
    result.append(str(arr.pop(idx)))

print("<"+", ".join(result)+">")