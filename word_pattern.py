# My Rating = 2
# https://leetcode.com/problems/word-pattern/


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        rec={}
        recReverse={}
        s = s.split()
        patternLen = len(pattern)
        if patternLen != len(s):
            return False
        for i in range(patternLen):
            if pattern[i] in rec:
                if rec[pattern[i]] != s[i]:
                    return False
            if s[i] in recReverse:
                if recReverse[s[i]] != pattern[i]:
                    return False
            rec[pattern[i]] = s[i]
            recReverse[s[i]] = pattern[i]
        return True