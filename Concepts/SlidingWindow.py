# Variable Length

# Question 3 - Longest Substring

def lengthOfLongestSubstring(self,s:str) -> int:
    l = 0
    longest = 0
    sett = set()
    n = len(s)

    for r in range(n):
        while s[r] in sett:
            sett.remove(s[l])
            l +=1

        w = (r-l)+1
        longest = max(longest, w)
        sett.add(s[r])

    return longest

def findMaxAverage(self,nums,k):
    n = len(nums)
    cur_sum = 0

    for i in range(k):
        cur_sum +=nums[i]

    max_avg = cur_sum/k

    for i in range(k, n):
        cur_sum +=nums[i]
        cur_sum -=nums[i-k]

        avg = cur_sum/k
        max_avg = max(max_avg, avg)
