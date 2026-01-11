#No. 1546 평균

N=int(input())
arr=list(map(int, input().split()))
max=max(arr)

sum=0
for i in range(N):
    sum+=arr[i]/max*100
    #문제에서 '모든 점수'를 점수/최댓값*100을 한다고 했으므로 max값도 똑같이 max/max*100해줘야 함. 

print(sum/N)


#No. 1157 단어공부
S=input().upper()

arr=[0 for i in range(26)]
for i in range(len(S)):
    a=ord(S[i])
    # 문자(열)을 아스키코드로 변환=ord()
    # 반대로 아스키코드를 문자(열)로 변환은 str()
    arr[a-65]+=1

max=0
result=""
for i in range(26):
    if(max<arr[i]):
        result=chr(i+65)
        max=arr[i]
    elif(max==arr[i] and arr[i]!=0):
        result="?"

print(result.upper())


#1316 그룹 단어 체커
N=int(input())
result=0

for i in range(N):
    flag=False
    S=input()
    check=[]
    for j in range(len(S)):
        if j==len(S)-1:
            flag=True
            
        if S[j] not in check:
           check.append(S[j])
        elif S[j] in check and S[j]==S[j-1]:
            continue
        elif S[j] in check and S[j]!=S[j-1]:
            flag=False
            break        
            
    if flag==True:
        result+=1
        

print(result)




    
