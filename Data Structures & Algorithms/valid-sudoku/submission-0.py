class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = [set() for _ in range(9)]
        column_set = [set() for _ in range(9)]
        box_set = [set() for _ in range(9)]

        for row in range(9):
            for column in range(9):
                value = board[row][column]

                if value == ".":
                    continue

                box_index = (row // 3) * 3 + (column // 3)

                if (
                    value in row_set[row]
                    or value in column_set[column]
                    or value in box_set[box_index]
                ):
                    return False

                row_set[row].add(value)
                column_set[column].add(value)
                box_set[box_index].add(value)

        return True
        
        