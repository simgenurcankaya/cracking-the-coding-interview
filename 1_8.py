import copy


def makeZero(matrix,i,j):
    for x in range(len(matrix)):
        matrix[i][x] = 0;
    for x in range(len(matrix[0])):
        matrix[x][j] = 0;

    return matrix;
            
def zeroMatrix(matrix):
    retval =copy.deepcopy(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if(matrix[i][j] == 0):
                retval = makeZero(retval,i,j)
    return retval

t = [['a', 'b', 'c'],
     ['d', 'e', 'f'], 
     [0, 'h', 'i']]


s = [[1,0],[2,3]]

d = [
            [1, 2, 3, 4, 0],
            [6, 0, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 0, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ]

print(zeroMatrix(t))
print(zeroMatrix(s))
print(zeroMatrix(d))


# [[0, 'b', 'c'], [0, 'e', 'f'], [0, 0, 0]]
# [[0, 0], [2, 0]]
# [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [11, 0, 13, 14, 0], [0, 0, 0, 0, 0], [21, 0, 23, 24, 0]]