
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist_points = []
        for point in points:
            dist = point[0]**2 + point[1]**2  # sqrt 생략 가능
            dist_points.append((dist, point))
        
        dist_points.sort()  # 거리 오름차순
        return [p for _,p in dist_points[:k]]
        
        