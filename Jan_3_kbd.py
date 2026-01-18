# 1546 평균

'''
n=int(input())
a=list(map(int,input().split()))
max_val=max(a)


for i in range(n):
#    a[i]=a[i]/(max(a)*100)
# a[i]의 값을 루프 안에서 수정하면, 다음 루프 때 최댓값이 달라질 수 있다.
    a[i]=a[i]/max_val*100


print(sum(a)/n) '''


# 1157 단어공부

'''a=input().upper()
a_list=list(set(a))
cnt=[]

for i in a_list:
    count=a.count(i)
    cnt.append(count)

if cnt.count(max(cnt)) >=2 :
    print("?")
else:
    print(a_list[(cnt.index(max(cnt)))])'''

# 1316 그룹단어체커
'''
n=int(input())
group_word=0

for _ in range(n):
    word=input()

    for i in range(len(word)):
        if i != len(word) -1:
            if word[i]== word[i+1]:
                pass
            elif word[i] in word[i+1:]:
                break
        else:
            group_word+=1

print(group_word) '''