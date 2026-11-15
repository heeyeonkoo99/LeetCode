class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m,n=len(matrix),len(matrix[0])

        l,r=0,m*n-1
        while l<=r:
            mid=(l+r)//2
            row,col=divmod(mid,n)
            if matrix[row][col]==target:
                return True
            elif matrix[row][col]<target:
                l=mid+1
            else:
                r=mid-1
        return False

        