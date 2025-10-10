class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_products = [1] * n
        right_products = [1] * n
        res = [1] * n

        # 왼쪽 곱 누적
        for i in range(1, n):
            left_products[i] = left_products[i-1] * nums[i-1]

        # 오른쪽 곱 누적
        for i in range(n-2, -1, -1):
            right_products[i] = right_products[i+1] * nums[i+1]

        # 결과 계산
        for i in range(n):
            res[i] = left_products[i] * right_products[i]

        return res
