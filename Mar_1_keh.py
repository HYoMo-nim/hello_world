# No. 11723  집합 ------------------------------

import sys
input=sys.stdin.readline

x=int(input())
arr=set()

for i in range(x):
    y=input().strip().split()

    if len(y)==1:
        if y[0]=="all":
            arr=set([j for j in range(1, 21)])
        else:
            arr=set()
    else:
        a, b=y[0], y[1]
        b=int(b)
        if a=="add":
            arr.add(b)

        elif a=="remove":
            arr.discard(b)

        elif a=="check":
            if b in arr:
                print(1)
            else:
                print(0)
                
        elif a=="toggle":
            if b in arr:
                arr.discard(b)
            else:
                arr.add(b)


# No. 10845  큐 ------------------------------

import sys
input=sys.stdin.readline

x=int(input())
arr=[]

for i in range(x):
    y=input().strip().split()

    if len(y)==2:
        a, b=y[0], y[1]
        b=int(b)
        arr.append(b)
        
    else:
        if y[0]=="pop":
            if len(arr)==0:
                print(-1)
            else:
                print(arr.pop(0))
                
        elif y[0]=="size":
            print(len(arr))
            
        elif y[0]=="empty":
            if len(arr)==0:
                print(1)
            else:
                print(0)
                
        elif y[0]=="front":
            if len(arr)==0:
                print(-1)
            else:
                print(arr[0])
                
        elif y[0]=="back":
            if len(arr)==0:
                print(-1)
            else:
                print(arr[len(arr)-1])


# No. 10816  숫자카드2 ------------------------------

import sys
input=sys.stdin.readline

arr={}
x=int(input())
y=input().strip().split()
for i in range(x):
    num=int(y[i])
    arr[num]=arr.get(num, 0)+1

a=int(input())
b=input().strip().split()
for i in range(a):
    result=int(b[i])
    print(arr.get(result, 0), end=" ")

