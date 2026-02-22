# No. 2839    설탕 배달--------------------------------------
n = int(input())
count = 0
while n > 0:
    if n % 5 == 0:
        count += n // 5
        n = 0
    elif n >= 3:
        count += 1
        n -= 3
    else:
        count = -1
        break
print(count)

# No. 9012 괄호 　　　https://www.acmicpc.net/problem/9012
n = int(input())
for _ in range(n):
    s = input()
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if not stack:
                stack.append(c)
                break
            else:
                stack.pop()
    print('YES' if not stack else 'NO')

# No. 10828  스택 　　　https://www.acmicpc.net/problem/10828
n = int(input())
stack = []
for _ in range(n):
    command = input().split()
    if command[0] == 'push':
        stack.append(command[1])
    elif command[0] == 'pop':
        print(stack.pop() if stack else -1)
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        print(0 if stack else 1)
    elif command[0] == 'top':
        print(stack[-1] if stack else -1)
        