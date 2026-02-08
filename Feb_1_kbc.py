# 2839 설탕 배달
'''
n=int(input())

if n%5==0:
    print(n//5)

else:
    p=0
    while n>0:
        n-=3
        p+=1

        if n%5==0:
            p+=n//5
            print(p)
            break

        elif n==1 or n==2:
            print(-1)
            break

        elif n==0:
            print(p)
            break'''

# 9012 괄호
'''
n=int(input())

for i in range(n):
    a=input()
    stack=[]
    is_vps=True
    
    for j in a:
        if j=='(':
            stack.append(j)
        elif j==')':
            if stack:
                stack.pop()
            else:
                is_vps=False
                break

    if is_vps and not stack: #스택이 비어 있는가? 
        print("YES")
    else:
        print("NO")
'''

# 10828 스택 
'''
import sys
input=sys.stdin.readline

n = int(input())

stack=[]
for i in range(n):
    a = input().split()

    if a[0]=='push':
        stack.append(a[1])

    elif a[0]=='pop':
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())

    elif a[0] == 'size':
        print(len(stack))

    elif a[0] == 'empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)

    elif a[0] == 'top':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])
'''