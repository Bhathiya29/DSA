class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        p1 = 0

        for p2 in range(len(nums)):
            if nums[p2] != 0:
                nums[p1], nums[p2] = nums[p2], nums[p1]
                p1 += 1
            
                
        