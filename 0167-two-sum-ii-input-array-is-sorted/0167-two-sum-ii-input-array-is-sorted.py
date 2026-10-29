from collections import defaultdict
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        

        d={}
        numbers.sort()
        for i,v in enumerate(numbers):
            if target-v in d:
                print(d[v],i+1)
                return [d[v],i+1]
            d[v].append(i+1)
        