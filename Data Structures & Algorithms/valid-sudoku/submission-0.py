class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for row in range(9):
            for col in range(9):
                val = board[row][col]
                if val == ".":
                    continue

                row_key = (val, "row", row)
                col_key = (val, "col", col)
                box_key = (val, "box", row // 3, col // 3)

                if row_key in seen or col_key in seen or box_key in seen:
                    return False

                seen.add(row_key)
                seen.add(col_key)
                seen.add(box_key)
        return True
