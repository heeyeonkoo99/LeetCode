class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        res = []
        greatest = max(candies)

        for candy in candies:
            res.append(candy + extraCandies >= greatest)

        return res