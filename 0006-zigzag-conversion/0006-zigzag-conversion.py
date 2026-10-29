class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res=""
        if numRows>len(s) or numRows==1:
            return s
        temp=[""]*numRows
        print(temp)

        go_up=False
        idx=0
        for i in range(len(s)):
            if go_up==False:
                
                temp[idx]+=s[i]
                idx+=1
                if idx==numRows-1:
                    go_up=not go_up
            else:
                
                temp[idx]+=s[i]
                idx-=1
                if idx==0:
                    go_up=not go_up
            
        print(temp)

        return "".join(temp)
        