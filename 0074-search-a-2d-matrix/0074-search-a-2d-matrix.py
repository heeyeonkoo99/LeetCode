class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m,n=len(matrix),len(matrix[0])

        l,r=0,m*n-1
        while l<=r:
            mid=(l+r)//2
            row,col=divmod(mid,n)
            
            print(row,col)
            if matrix[row][col]<target:
                l=mid+1
            elif matrix[row][col]>target:
                r=mid-1
            else:
                return True
        return False
        