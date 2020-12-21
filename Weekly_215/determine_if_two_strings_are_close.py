# My Rating = 5
# https://leetcode.com/contest/weekly-contest-215/problems/determine-if-two-strings-are-close/

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        word1Rec = {}
        word2Rec = {}
        for i in word1:
            if i in word1Rec:
                word1Rec[i] += 1
            else:
                word1Rec[i] = 1
        for i in word2:
            if i in word2Rec:
                word2Rec[i] += 1
            else:
                word2Rec[i] = 1
        for i in word1Rec:
            if i not in word2Rec:
                return False
        for i in word2Rec:
            if i not in word1Rec:
                return False
        for i in word1Rec.values():
            if i not in word2Rec.values():
                return False
        for i in word2Rec.values():
            if i not in word1Rec.values():
                return False
        return True