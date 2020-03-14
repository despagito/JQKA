import unittest

from test import Solution


class Test(unittest.TestCase):
    def test_valid(self):
        board = [
            ['J0', 'Q1',    0,  0],
            [0,    'K2',    0,  0],
            [0,    'A3',    0,  0],
            [0,     0,      0,  0]
        ]
        sol = Solution()
        res_row = sol.valid(board, 'J1', [0, 2])
        self.assertEqual(res_row, False)

        res_col = sol.valid(board, 'J1', [2, 0])
        self.assertEqual(res_col, False)

        res_diag1 = sol.valid(board, 'A2', [0, 3])
        self.assertEqual(res_diag1, False)

        res_diag2 = sol.valid(board, 'Q2', [3, 3])
        self.assertEqual(res_diag2, False)

        # Positive
        res_row_true = sol.valid(board, 'K3', [0, 2])
        self.assertEqual(res_row_true, True)

        res_col_true = sol.valid(board, 'K1', [2, 0])
        self.assertEqual(res_col_true, True)

        diag1_true = sol.valid(board, 'K2', [0, 3])
        self.assertEqual(diag1_true, True)

        diag2_true = sol.valid(board, 'Q1', [2, 2])
        self.assertEqual(diag2_true, True)

if __name__ == '__main__':
    unittest.main()