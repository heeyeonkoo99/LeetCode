class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        result=[]
        left,right=0,len(matrix[0])-1
        top,bottom=0, len(matrix)-1

        while left<=right and top<=bottom:
            for i in range(left,right+1):
                result.append(matrix[top][i])
            top+=1

            for i in range(top,bottom+1):
                result.append(matrix[i][right])
            right-=1

            if top <= bottom:  # 아직 행이 남아 있다면
                # 오른쪽 → 왼쪽
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1

            if left <= right:  # 아직 열이 남아 있다면
                # 아래쪽 → 위쪽
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1
        return result

        