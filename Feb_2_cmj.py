# No. 11399  ATM---------------------------------------------------
n= int(input())
arr = list(map(int, input().split()))
arr.sort()
result = 0
time = 0
for i in range(n):
    time += arr[i]
    result += time
print(result)

# No. 11047  동전 0--------------------------------------------------
n, k = map(int, input().split()) # N : 화폐 종류수, K : 거슬러 줄 돈

coins = []                     # 계산대에 있는 화폐들을 리스트의 형태로 입력받음
for _ in range(n):
    coins.append(int(input()))
coins.sort(reverse=True)

count = 0
for coin in coins: 
    if k >= coin:    # 거슬러 줄 돈이 화폐보다 크거나 같을 때
        count += k // coin       # 거슬러 줄 돈을 화폐로 나눈 몫을 count에 더함
        k %= coin             
print(count)

# No. 1920    수 찾기------------------------------------------------
n = int(input())
n_list = list(map(int, input().split()))
n_list.sort()
m = int(input())
m_list = list(map(int, input().split()))

for m in m_list:
    left, right = 0, n - 1
    
    while left <= right:
        mid = (left + right) // 2
        if m > n_list[mid]:
            left = mid + 1
        elif m < n_list[mid]:
            right = mid - 1
        else:
            left = mid
            right = mid
            break
            
    if left == mid and right == mid:
        print(1)
    else:        
        print(0)
    