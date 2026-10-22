from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        need = Counter(t)
        window = {}

        have = 0
        required = len(need)

        res = [-1,-1]
        resLen = float("inf")

        l = 0

        for r, c in enumerate(s):
            window[c] = window.get(c,0) +1

            if c in need and window[c] == need[c]:
                have+=1
            
            while have == required:
                if (r-l+1) < resLen:
                    resLen = r-l+1
                    res = [l,r]
                
                window[s[l]] -=1

                if s[l] in need and window[s[l]] < need[s[l]]:
                    have -=1
                
                l+=1
        if resLen == float("inf"):
            return ""
        
        return s[res[0]:res[1]+1]