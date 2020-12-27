# My Rating = 1
# https://leetcode.com/contest/weekly-contest-221/problems/determine-if-string-halves-are-alike/

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = {'a','i','e','o','u','A','E','I','O','U'}
        left=0
        right=0
        for i in range(int(len(s)/2)):
            if s[i] in vowels:
                left += 1
        for i in range(int(len(s)/2),len(s)):
            if s[i] in vowels:
                right += 1
        return left==right