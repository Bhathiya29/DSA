class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        L = 0
        R = len(nums)-1

        res = []

        while L <= R:
            if abs(nums[L]) > abs(nums[R]):
                res.append(nums[L]**2)
                L+=1
            else:
                res.append(nums[R]**2)
                R-=1
        
        res.reverse()

        return res
