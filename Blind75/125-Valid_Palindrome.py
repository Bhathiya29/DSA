class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s2 =""

        for l in s:
            if l.isalnum():
                s2+=l.lower()
        
        #checking for palindrome
        p1,p2 = 0, len(s2)-1
        while p1 < p2:
            if s2[p1] != s2[p2]: return False
            p2 -=1
            p1 +=1

        
        return True
