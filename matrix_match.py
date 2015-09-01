import random

w1 = int(raw_input(">>> w1: "))
h1 = int(raw_input(">>> h1: "))
w2 = int(raw_input(">>> w2: "))
h2 = int(raw_input(">>> h2: "))

r1 = int(raw_input(">>> r1: "))
r2 = int(raw_input(">>> r2: "))

# w1 = 20
# h1 = 20
# w2 = 3
# h2 = 3

matrix = [[random.randint(r1, r2) for x in range(w1)] for x in range(h1)]
pattern = [[random.randint(r1, r2) for x in range(w2)] for x in range(h2)]


def matchMatrix(matrix1, matrix2):
    print 'Match Matrix start:\n '
    results = []
    temp = []
    for x in matrix2:
        for y in x:
            temp.append(y)

    indexOfX = 0
    for x in matrix1:
        if indexOfX >= (h1-h2+1):
            break
        indexOfY = 0
        for y in x:
            if indexOfY >= (w1-w2+1):
                break
            count = 0
            for z in matrix2:
                subMatrix = matrix[indexOfX+count]
                count+=1
                size = len(z)
                subX = subMatrix[indexOfY:indexOfY+size] 
                if z != subX:
                    break
                if count == h2:
                    results.append((indexOfX, indexOfY))
            indexOfY+=1
        indexOfX+=1
    return results

for x in pattern:
    print x
for x in matrix:
    print x

print 'Ans:\n%s' % (matchMatrix(matrix, pattern))