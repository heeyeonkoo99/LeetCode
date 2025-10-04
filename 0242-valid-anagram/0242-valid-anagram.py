
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict={}
   
        for i in s:
            if i not in dict:
                dict[i]=1
            else:
                dict[i]+=1

        for i in t:
            if i in dict and dict[i]!=0:
                dict[i]-=1

            else:
                return False
        return sum(dict.values())==0
    

        