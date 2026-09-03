class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1 or numRows>=len(s):
            return s
        current_row=0
        going_down=False
        ans=[""]*numRows
        for i in s:
            if current_row==0 or current_row==numRows-1:
                going_down=not going_down
            ans[current_row]+=i
            current_row+=1 if going_down else -1
        return "".join(ans)

        