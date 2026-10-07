# Concept - Recursive Backtracking

# Question 78 - All subsets

def subsets(self,nums):
    n = len(nums)
    res, sol = [],[]

    def backtrack(i):
        if i == n:
            res.append(sol[:])
            return
        
        # Don't pick nums at i
        backtrack(i+1)
        
        # Pick nums at i
        sol.append(nums[i])
        backtrack(i+1)
        sol.pop()


    backtrack(0)
    return res

