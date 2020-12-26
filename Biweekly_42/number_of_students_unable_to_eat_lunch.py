# My Rating = 2
# https://leetcode.com/contest/biweekly-contest-42/problems/number-of-students-unable-to-eat-lunch/

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        total = len(students)
        oneCount = sum(students)
        zeroCount = total - oneCount
        for i in sandwiches:
            if i == 0:
                zeroCount -= 1
                if zeroCount<0:
                    return oneCount + zeroCount + 1
            else:
                oneCount -= 1
                if oneCount<0:
                    return oneCount + zeroCount + 1
        return 0