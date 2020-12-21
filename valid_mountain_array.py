# My Rating = 3
# https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/570/week-2-december-8th-december-14th/3561/

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)<3:
            return False
        phase=-1
        check1=False
        for ele in arr:
            if phase==-1:
                phase=0
                prev=ele
                pass
            elif phase==0:
                if prev>ele:
                    phase = 1
                elif prev==ele:
                    return False
                else:
                    check1=True
                prev=ele
            elif phase==1:
                if not prev>ele:
                    return False
                prev=ele
        return phase==1 and check1