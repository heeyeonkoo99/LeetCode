class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        초기생각: 먼가 key-value형태의 dict로 만들어서 for문을 돌리면 만들수 있을것같은데,,
                 그렇다면, for문을 len(digits)만큼 만들면되려나,,?
        풀이: dict를 만들어서 dfs로 푸는게 맞다! 조건문을 잘 생각해보자!
        """
        answer=[]
        digitToChar={
             "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"}
        def backtracking(i, curStr):
            if len(digits)==len(curStr):
                answer.append(curStr)
                return
            for alphabet in digitToChar[digits[i]]:
                backtracking(i+1, curStr+alphabet)
        if digits:
            backtracking(0,"")
        return answer
        