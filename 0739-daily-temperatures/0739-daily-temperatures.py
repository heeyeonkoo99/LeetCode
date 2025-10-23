class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        res=[0]*len(temps)
        stack=[]

        for i,temp in enumerate(temps):
            while stack and temp>temps[stack[-1]]:
                index=stack.pop()
                res[index]=i-index
            stack.append(i)

        return res
                


        