class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        1. make a, b into decimal format
        2. add a and b 
        3. makt it into binary format
        """
        new_a=int(a,2)
        new_b=int(b,2)
        answer=new_a+new_b
        #print(new_a,new_b)
        answer=format(answer,"b")
        return answer