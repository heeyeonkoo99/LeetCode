class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res=[]

        for i in range(1,n+1):
            if i%3==0:
                if i%5==0:
                    res.append("FizzBuzz")
                else:
                    res.append("Fizz")
            else:
                if i%5==0:
                    res.append("Buzz")
                else:
                    res.append(str(i))


        return res
        