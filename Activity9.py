i = [1,2,3,4]
j = [6,8,7,4,0]
A = []
B = []
C = []
for x in i:
    if (x % 2 == 1):
        A.append(x)
#print(A)
for y in j:
    if (y % 2 == 0):
        B.append(y)
#print(B)

C=A+B
print(C)
