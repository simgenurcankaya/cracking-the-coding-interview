import unittest

def rotateMatrix(matrix):
    N = len(matrix[0])

    retval = []
    for i in range(N):
        dum = []
        for j in range(N):
            f = N-1-i
            dum.append(matrix[j][f])
        retval.append(dum)

    return retval



# a b     b d
# c d     a c 

# a b c       c f i
# d e f       b e h
# g h i       a d g 


t = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]

print(rotateMatrix(t))

x = [['a','b'],['c','d']]

print(rotateMatrix(x))


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ([
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [5, 10, 15, 20, 25],
            [4, 9, 14, 19, 24],
            [3, 8, 13, 18, 23],
            [2, 7, 12, 17, 22],
            [1, 6, 11, 16,21]
        ])
    ]

    def test_rotate_matrix(self):
        for [test_matrix, expected] in self.data:
            actual = rotateMatrix(test_matrix)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()