class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1 or numRows>=len(s):
            return s
        rows=[""] * numRows
        going_down=False
        current_row=0

        for c in s:
            rows[current_row]+=c
            if current_row==0 or current_row==numRows-1:
                going_down=not going_down
            current_row+=1 if going_down else -1
        return "".join(rows)