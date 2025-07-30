class Solution:
    def myPow(self, x: float, n: int) -> float:
        my_pow_num = pow(x, n)
        
        if my_pow_num > (pow(2, 31) - 1):
            my_pow_num = pow(2, 31) -1
        elif my_pow_num < (pow(2, 31)) * (-1):
            my_pow_num = pow(2, 31) * (-1)
            
        return my_pow_num