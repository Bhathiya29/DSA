class Solution:
    def maxArea(self, height: list[int]) -> int:
        p1, p2, maxArea = 0, len(height) - 1, 0

        while p1 < p2:
            # calculate the new MaxArea
            curArea = min(height[p1],height[p2]) * (p2 - p1)
            maxArea = max(maxArea, curArea)

            # we just have to move the smaller height inwards
            if height[p1] < height[p2]:
                p1+=1
            else:
                p2 -=1

        return maxArea