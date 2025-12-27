#No. 3052 나머지------------------------------------

a =[]

for i in range(10):
    n = int(input())
    a.append(n % 42)
    
a=set(a)
print(len(a))

#No. 2577 숫자의 개수--------------------------------

a = int(input())
b = int(input())
c = int(input())
d = a * b * c
d = str(d)
for i in range(10):
    print(d.count(str(i)))
    
#No. 8958 OX퀴즈-------------------------------------

A = int(input())
for i in range(A):
    B = input()
    score = 0
    sum = 0
    for j in B:
        if j == 'O':
            score += 1
            sum += score
        else:
            score = 0
    print(sum)
    
#No. 1978 소수 찾기-----------------------------------

n = int(input())
num = list(map(int, input().split()))
count = 0
for i in num:
    if i == 1:
        continue
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            break
    else:
        count += 1
print(count)

#No. 2750 수 정렬하기--------------------------------

n = int(input())
num = []
for i in range(n):
    num.append(int(input()))
num.sort()

for i in num:
    print(i)
    
#No. 2798 블랙잭------------------------------------

n, m = map(int, input().split())
num = list(map(int, input().split()))
result = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            total = num[i] + num[j] + num[k]
            if total <= m:
                result = max(result, total)
print(result)

#No. 2292 벌집--------------------------------------

n = int(input())
layer = 1
max_num = 1
while n > max_num:
    max_num += 6 * layer
    layer += 1
print(layer)
 