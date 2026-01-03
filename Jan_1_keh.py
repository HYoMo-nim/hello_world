#NO. 5622

sec=2
result=0

num=input()

for i in range(len(num)):
    if ord(num[i])==1:
        result+=sec
    elif ord(num[i])>=65 and ord(num[i])<=67:
        result+=sec+1
    elif ord(num[i])>=68 and ord(num[i])<=70:
        result+=sec+2
    elif ord(num[i])>=71 and ord(num[i])<=73:
        result+=sec+3
    elif ord(num[i])>=74 and ord(num[i])<=76:
        result+=sec+4
    elif ord(num[i])>=77 and ord(num[i])<=79:
        result+=sec+5
    elif ord(num[i])>=80 and ord(num[i])<=83:
        result+=sec+6
    elif ord(num[i])>=84 and ord(num[i])<=86:
        result+=sec+7
    else:
        result+=sec+8
        
print(result)


#NO. 2231
a=int(input())
result=0

for i in range(1, a):
    x=sum(map(int, str(i)))
    #i를 string으로 만들고(str(i)), str(i)의 각 자리를 int형으로 변환한 뒤, 전부 더하고 x에 저장
    #즉 i=198일 경우 (int)198에서 (string)198로 만들고, 각 자릿수(1, 9, 8)을 다시 int로 바꾸고 전부 더함=18
    if i+x==a:
          result=i
          break

print(result)


#NO. 15596
def solve(a: list):
    all=sum(a)
    return all
# ???????;;


#NO.2920
a=input()

if a=="1 2 3 4 5 6 7 8":
    print("ascending")
elif a=="8 7 6 5 4 3 2 1":
    print("descending")
else:
    print("mixed")
# 뭐 이딴걸 문제라고...


#NO.2581
sum=0
min=10000

a=int(input())
b=int(input())

for i in range(a, b+1):
    for j in range(2, i+1):
        if j==i:
            sum+=j
            if min>j:
                min=j
        if i%j==0:
            break

if min==10000 and sum==0:
    print("-1")
else:
    print(sum)
    print(min)


#NO.10813
n, m=map(int, input().split())

basket=[0]*n
result=""

for i in range(n):
    basket[i]=i+1

for i in range(m):
    x, y=map(int, input().split())
    num=basket[x-1]
    basket[x-1]=basket[y-1]
    basket[y-1]=num

for i in range(n):
    result+=str(basket[i])+" "

print(result)


#NO.1712
a, b, c=map(int, input().split())

if c-b<=0:
    print("-1")
else:
    result=a/(c-b)+1
    print(int(result))





