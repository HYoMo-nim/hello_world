# 11399 ATM
'''
n=int(input())
a=list(map(int,input().split()))

a.sort()
total=a[0]

for i in range(1,n):
    total+=a[i]
    for j in range(i):
        total=total+a[j]

print(total)
'''

# 11047 동전 0
'''
import sys
input = sys.stdin.readline

a=list(map(int,input().split()))
arr=[]

for i in range(a[0]):
    b=int(input())
    arr.append(b)

arr.sort(reverse=True)

balance=a[1]
coin=0

for i in range(len(arr)):
    if balance==0:
        break

    if balance>=arr[i]:
        coin+=balance//arr[i]
        balance=balance%arr[i]

print(coin) 
'''
