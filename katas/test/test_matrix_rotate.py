import unittest
from katas.matrix_rotate import rotate_matrix


class TestMatrixRotate(unittest.TestCase):
    matrix1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    matrix2 = [1]
    matrix3 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16],
    ]
    matrix4 = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25]
    ]
    matrix5 = []

    output1 = rotate_matrix(matrix1)
    output2 = rotate_matrix(matrix2)
    output3 = rotate_matrix(matrix3)
    output4 = rotate_matrix(matrix4)
    output5 = rotate_matrix(matrix5)

    def test1(self):
        self.assertEqual(self.output1, [
            [7, 4, 1],
            [8, 5, 2],
            [9, 6, 3]
        ])
        self.assertEqual(self.output2, [1])
        self.assertEqual(self.output3, [
            [13, 9, 5, 1],
            [14, 10, 6, 2],
            [15, 11, 7, 3],
            [16, 12, 8, 4]
        ])
        self.assertEqual(self.output4, [
            [21, 16, 11, 6, 1],
            [22, 17, 12, 7, 2],
            [23, 18, 13, 8, 3],
            [24, 19, 14, 9, 4],
            [25, 20, 15, 10, 5]
        ])
        self.assertEqual(self.output5, [])
