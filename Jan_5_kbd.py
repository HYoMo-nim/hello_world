# 2571 수 정렬하기 2
'''
import sys

input=sys.stdin.readline

n=int(input())
arr=[]

for i in range(n):
    a=int(input())
    arr.append(a)

set(arr)
arr.sort()

for i in arr:
    print(i)
'''

# 2941 크로아티아 알파벳
'''
import sys
input=sys.stdin.readline

arr=['c=','c-','dz=','d-','lj','nj','s=','z=']

a=(input().strip())

for i in arr:
    a=a.replace(i,'c')

print(len(a))

'''

# 1181 단어 정렬
'''
import sys

input=sys.stdin.readline

n=int(input().strip())
arr=[]

for i in range(n):
    a=input().strip()
    arr.append(a)

arr=sorted(set(arr))
arr.sort(key=lambda x: (len(x),x))
#1순위 2순위 

for a in arr:
    print(a)
'''
# 1193 분수 찾기(실패)
#아까워서 ㅠ
'''
n=int(input())
cnt=1
x=1
y=1

for i in range(n):
    if cnt==n:
        print(f"{x}/{y}")
        break
    
    if x==1:
        if y%2!=0:
            y+=1
            cnt+=1
            
        else:
            x+=1
            y-=1 
            cnt+=1
    
    elif y==1:
        if x%2==0:
            x+=1
            cnt+=1

        else:
            y+=1
            x-=1
            cnt+=1          

    else:
        y+=1
        x-=1
        cnt+=1


'''
# 1193 분수 찾기 
n=int(input())
line=1

while n>line:
    n-=line
    line+=1

if line%2==0:
    top=n
    bottom=line-n+1

else:
    top=line-n+1
    bottom=n

print(f"{top}/{bottom}")


# 11651 좌표 정렬하기 2
'''
import sys
input=sys.stdin.readline

n=int(input())
arr=[]

for i in range(n):
    a,b=map(int,input().split())
    arr.append((a,b))

arr.sort(key=lambda x: (x[1],x[0]))

for i in range(n):
    print(arr[i][0],arr[i][1])
'''

# 2563 색종이
'''
n=int(input())
arr=[[0]*100 for _ in range(100)]

for _ in range(n):
    a,b=map(int,input().split())
    for j in range(a-1,a+9):
        for k in range(b-1,b+9):
            arr[j][k]=1

total=sum(row.count(1) for row in arr)
print(total)
'''

# 25206 너의 평점은 
'''
total=0
total2=0

for i in range(20):
    a,b,c=input().split()
    b=float(b)

    grade = {

        "A+":4.5, "A0":4.0, "B+":3.5, "B0":3.0,
        "C+":2.5, "C0":2.0, "D+":1.5, "D0":1.0, "F":0.0

    }

    if c=="P":
        continue

    total+=b*grade[c]
    total2+=b

print(f"{total/total2:.6f}")
'''