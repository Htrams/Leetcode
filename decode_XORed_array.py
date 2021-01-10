# My Rating = 1
# https://leetcode.com/contest/weekly-contest-223/problems/decode-xored-array/

class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        output = []
        output.append(first)
        for num in encoded:
            first = first^num
            output.append(first)
        return output