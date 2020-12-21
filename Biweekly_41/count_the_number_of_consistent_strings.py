# My Rating = 1
# https://leetcode.com/contest/biweekly-contest-41/problems/count-the-number-of-consistent-strings/

# You are given a string allowed consisting of distinct characters and an array of strings words. 
# A string is consistent if all characters in the string appear in the string allowed.
# Return the number of consistent strings in the array words.

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        record=set()
        count=0
        for char in allowed:
            record.add(char)
        for word in words:
            flag=0
            for char in word:
                if char not in record:
                    flag=1
                    break
            if not flag:
                count += 1
        return count
        