import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        """ 
        풀이: 아래 방식은 효율적으로 2의 거듭제곱여부를 판단하는 방식
        어떤 수가 2의 거듭제곱이라면 n에서 가장 왼쪽의 1 하나만 있고, n-1은 그 자리보다 낮은 비트가 모두 1이 됨.
        코드: 
        if n<=0:
            return False
        return (n&(n-1))==0
        """
        if n==0:
            return False
        while n%2==0:
            n//=2
        return n==1
        
        




        