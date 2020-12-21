# My Rating = 5
# https://leetcode.com/explore/challenge/card/november-leetcoding-challenge/566/week-3-november-15th-november-21st/3534/

class Solution:
    def lcm(self,a, b):
        return abs(a*b) // math.gcd(a, b)
    
    def mirrorReflection(self, p: int, q: int) -> int:
        if p%q==0 and (p//q)%2 == 0:
            return 2
        lcm = self.lcm(p,q)
        if (lcm//p) % 2 == 1:
            if (lcm//q) % 2 == 0:
                return 2
            else:
                return 1
        else:
            return 0