class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1 or len(s)>=numRows:
            return s

        going_down=False
        row=[""] *numRows
        current_row=0
        for i in s:
            row[current_row]+=i
            if current_row==0 or current_row==numRows-1:
                going_down=not going_down
            current_row+=1 if going_down else -1
        return "".join(row)
        