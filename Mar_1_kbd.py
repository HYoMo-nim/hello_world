# 11723 집합

import sys
input=sys.stdin.readline

M=int(input())
S=set()
ALL=set(range(1,21)) #미리 집합 만들어두면 단축 가능 

for _ in range(M):
    temp=input().split() 
  
    if len(temp)==1:
        if temp[0]=="all":
            S=ALL.copy() #생성함수 set([인자])
        else: 
            S=set() #empty
    
    else:
        cmd,x=temp[0],int(temp[1])
        if cmd=="add":
            S.add(x)
        elif cmd=="remove":
            S.discard(x)
        elif cmd=="check":
            print(1 if x in S else 0)
        elif cmd=="toggle":
            if x in S:
                S.discard(x)
            else:
                S.add(x)

# 10845 큐

from collections import deque 
import sys
input=sys.stdin.readline

N=int(input())
dq=deque()

for _ in range(N):
    temp=input().split()
    if temp[0] == 'push':
        dq.append(temp[1])
    elif temp[0]=='pop':
        if len(dq)!=0:
            print(dq.popleft())
        else:
            print(-1)
    elif temp[0]=='size':
        print(len(dq))
    elif temp[0]=='empty':
        if len(dq)==0:
            print(1)
        else:
            print(0)
    elif temp[0]=='front':
        if len(dq)!=0:
            print(dq[0])
        else:
            print(-1)
    elif temp[0]=='back':
        if len(dq)!=0:
            print(dq[-1])
        else:
            print(-1)


# 10816 숫자카드 2 
import sys
input=sys.stdin.readline

N=int(input())
N_s=list(map(int,input().split()))

M=int(input())
M_s=list(map(int,input().split()))

n_dic={}

for n in N_s:
    if n in n_dic:
        n_dic[n]+=1
    else:
        n_dic[n]=1

for m in M_s:
    if m in n_dic:
        print(n_dic[m],end=" ")

    else:
        print(0,end=" ")