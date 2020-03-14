from typing import List

class Solution:
    def JQKA(self, board: List[List[str]], cards: List[str]) -> None:

        for card in cards:

            # for each card, find all possible place to fill
            for i in range(4):
                for j in range(4):
                    if board[i][j] == 0:

                        if self.valid(board, card, [i, j]):
                            board[i][j] = card
                            self.JQKA(board, cards[1:]) # calculate the rest of positions
                        else:
                            board[i][j] = 0
        return board

    def valid(self, board: List[List[str]], card: str, location: List[int]) -> bool:
        i, j = location[0], location[1]
        for x in range(4):
            # Find conflicts in this row
            thisRow = board[x][j]
            if thisRow != 0 and (card[0] in thisRow or card[1] in thisRow):
                return False

            # Find conflicts in this column
            thisCol = board[i][x]
            if thisCol != 0 and (card[0] in thisCol or card[1] in thisCol):
                return False

            # Find conflicts in \
            if i == j:
                thisDiag1 = board[x][x]
                if thisDiag1 != 0 and (card[0] in thisDiag1 or card[1] in thisDiag1):
                    return False

            # Find conflicts in /
            if i + j == 3:
                thisDiag2 = board[x][3-x]
                if thisDiag2 != 0 and (card[0] in thisDiag2 or card[1] in thisDiag2):
                    return False
        return True

board = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

# numbers 0123 means different suits
cards = ['J0', 'J1', 'J2', 'J3', 'Q0', 'Q1', 'Q2', 'Q3', 'K0', 'K1', 'K2', 'K3', 'A0', 'A1', 'A2', 'A3']
res = Solution().JQKA(board, cards)
print(res)
