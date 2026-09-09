class Solution:
    def maxArea(self, height: List[int]) -> int:
        temp=0
        area=0

        l,r=0,len(height)-1

        while l<r:
            area=min(height[l],height[r])*(r-l)
            temp=max(temp,area)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1



        return temp