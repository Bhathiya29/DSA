def search(self, nums, target):
        low,high = 0, len(nums)-1

        while low <= high:
            mid = low+(high - low)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid+1
            else:
                high = mid -1
                
        return -1