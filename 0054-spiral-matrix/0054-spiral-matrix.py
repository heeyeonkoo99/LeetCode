class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res=[]
        m,n=len(matrix),len(matrix[0])
        left,right=0,n-1
        up,down=0,m-1


        while left<=right and up<=down:

            for j in range(left,right+1):
                res.append(matrix[up][j])
            up+=1

            for i in range(up,down+1):
                res.append(matrix[i][right])
            right-=1

            if up<=down:
                for j in range(right,left-1,-1):
                    res.append(matrix[down][j])
                down-=1


            if left<=right:
                for i in range(down,up-1,-1):
                    res.append(matrix[i][left])
                left+=1


        return res
        