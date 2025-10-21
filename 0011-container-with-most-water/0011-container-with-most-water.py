class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r=0,len(height)-1
        width=len(height)-1
        maxi=0
        while l<r:
            area=min(height[l],height[r])*width
            maxi=max(maxi,area)

            if height[l]<height[r]:
                l+=1
            else:
                r-=1
            width-=1
        return maxi
        