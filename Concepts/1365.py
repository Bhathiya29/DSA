class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        temp = sorted(nums)

        hash_map = {}

        for i, num in enumerate(temp):
            if num not in hash_map:
                hash_map[num] = i
            
        res = []

        for i in nums:
            res.append(hash_map[i])
            
        return res