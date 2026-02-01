# 1월 5주차 (1/26~2/1)
# No. 2751      수 정렬하기2 　-------------------------------------------------------------
n = int(input())
numbers = []
for _ in range(n):
    numbers.append(int(input()))
numbers.sort()

for number in numbers:
    print(number)

# No. 2941      크로아티아 알파벳----------------------------------------------------------
croatian = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
word = input()
for c in croatian:
    word = word.replace(c, '*')
print(len(word))

# No. 1181      단어 정렬 ------------------------------------------------------------
n = int(input())
words = set()
for _ in range(n):
    words.add(input())
words = list(words)
words.sort(key=lambda x: (len(x), x))
print('\n'.join(words))

# No. 1193      분수찾기------------------------------------------------------------
x = int(input())
line = 1
while x > line:
    x -= line
    line += 1
if line % 2 == 0:
    numerator = x
    denominator = line - x + 1
else:
    numerator = line - x + 1
    denominator = x
print(f"{numerator}/{denominator}")

# No. 11651    좌표 정렬하기2   ------------------------------------------------------  
n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
points.sort(key=lambda x: (x[1], x[0]))
for point in points:
    print(point[0], point[1])
    
# No. 2563      색종이 ----------------------------------------------------------------
paper = [[0] * 100 for _ in range(100)]
n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            paper[i][j] = 1
print(sum(sum(row) for row in paper))

# No. 25206    너의 평점은 -1 --------------------------------------------------------------
grade_dict = {
    "A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0,
    "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0,
    "F": 0.0
}

sum_score = 0
sum_credit = 0 
for _ in range(20):
    subject, credit, grade = input().split()
    credit = float(credit)
    if grade != "P":
        sum_score += credit * grade_dict[grade]
        sum_credit += credit
gpa = sum_score / sum_credit
print(f"{gpa:.6f}")
