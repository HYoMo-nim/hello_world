# No. 5622     다이얼       
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
a = input()
ret = 0
for j in range(len(a)):
    for i in dial:
        if a[j] in i:
            ret += dial.index(i)+3
print(ret)

# No. 2231      분해합
n = int(input())  

for i in range(1, n+1): 
    num = sum((map(int, str(i))))  
    num_sum = i + num 

    if num_sum == n:
        print(i)
        break
    if i == n: 
        print(0)
        
# No. 15596    정수 N개의 합
def solve(a):
    ret = 0
    for i in a:
        ret += i
    return ret

# No. 2920     음계
a = list(map(int, input().split()))
if a == [1, 2, 3, 4, 5, 6, 7, 8]:
    print("ascending")
elif a == [8, 7, 6, 5, 4, 3, 2, 1]:
    print("descending")
else:
    print("mixed")
    
# No. 2581      소수 
m = int(input())
n = int(input())
prime = []
for i in range(m, n+1):
    if i == 1:
        continue
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            break
    else:
        prime.append(i)
if len(prime) == 0:
    print(-1)
else:
    print(sum(prime))
    print(min(prime))
    
# No. 10813    공 바꾸기  
n, m = map(int, input().split())
basket = [i for i in range(1, n+1)]
for _ in range(m):
    i, j = map(int, input().split())
    basket[i-1], basket[j-1] = basket[j-1], basket[i-1]
print(' '.join(map(str, basket)))

# No. 1712       손익분기점
a, b, c = map(int, input().split())
if b >= c:
    print(-1)
else:
    print(a // (c - b) + 1)
     