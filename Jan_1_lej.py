# No. 5622 다이얼

num = input()
time = 0
dial = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

for i in num:
    for j in dial:
        if i in j:
            num = dial.index(j) + 3
            time += num

print(time)



# No. 2231 분해합

n = int(input())
total = 0

for i in range(1, n+1):
    a  = list(map(int, str(i)))
    total = i + sum(a)

    if total == n:
        print(i)
        break
    if i == n:
        print(0)
        break



# No. 15596 정수 N개의 합(검색해봄)

def solve(x): 
    ans = 0 # 누적 합을 저장하는 변수
    for i in x:
            ans += i
    return ans



# No. 2920 음계

num = list(map(int, input().split()))

if num == [1, 2, 3, 4, 5, 6, 7, 8]:
    print("ascending")
elif num == [8, 7, 6, 5, 4, 3, 2, 1]:
    print("descending")
else:
    print("mixed")



# No. 2581 소수

m = int(input())
n = int(input())
A =  [ ]

for i in range(m, n+1):
    e=0
    if i>1:
        for j in range(2,i):
            if i%j==0:
                e+=1
                break
        if e==0:
            A.append(i)

if len(A)<1:
    print(-1)
else:
    print(sum(A))
    print(min(A))



# No. 10813 공 바꾸기

n, m = map(int, input().split())
A = list(range(1, n+1))

for i in range(m):
    i, j = map(int, input().split())
    A[i-1], A[j-1] = A[j-1], A[i-1]

for num in A:
    print(num, end= ' ')



# No. 1712 손익분기점

x, y, z = map(int, input().split())

if y >= z:
    print(-1)
else:
    total_cost = x # 총 비용
    total_revenue = 0  # 총 수익
    salse_rate = 0 # 손익 판매량

    while total_cost >= total_revenue:
        salse_rate += 1
        total_cost += y
        total_revenue += z
    print(salse_rate)