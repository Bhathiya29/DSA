def maxSubArray(self, nums):
        maxsum = nums[0]
        currSum = 0

        for n in nums:
            if currSum < 0:
                currSum = 0
            currSum+=n
            maxsum = max(maxsum,currSum)
        return maxsum