class Solution:
    def isValidSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]  # 0..8 for the 9 sub-boxes

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue

                box_id = (r // 3) * 3 + (c // 3)

                if val in rows[r] or val in cols[c] or val in boxes[box_id]:
                    return False

                rows[r].add(val)
                cols[c].add(val)
                boxes[box_id].add(val)

        return True
