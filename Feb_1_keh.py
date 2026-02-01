

# No. 2839 설탕 배달 --------------------------

a=int(input())
result=5001

for i in range(a//5+1):
    x=i*5
    if (a-x)%3==0:
        y=(a-x)//3+i
        result=min(result, y)

if result==5001: result=-1
print(result)


# No. 9012 괄호 --------------------------

a=int(input())

for i in range(a):
    s=input()
    flag=0
    x=0
    y=0
    for j in range(len(s)):
        if s[j]=='(':
             x+=1
        elif s[j]==')':
            if x>y:
                  y+=1
            else:
                   break
        flag+=1       

    if x==y and flag==len(s):
        print("YES")
    else:
        print("NO")


# No. 10828 스택 --------------------------

import sys
input=sys.stdin.readline

a=int(input().rstrip())
stack=[]

for i in range(a):
    s=input().rstrip()
    arr=s.split(" ")
    
    if(arr[0]=="push"): stack.append(arr[1])
    
    elif(arr[0]=="pop"):
        if len(stack)==0:
            print("-1")
        else:
            print(stack.pop())

    elif(arr[0]=="size"):
        print(len(stack))

    elif(arr[0]=="empty"):
        if len(stack)==0:
            print("1")
        else:
            print("0")

    elif(arr[0]=="top"):
        if len(stack)==0:
            print("-1")
        else:
            print(stack[-1])

