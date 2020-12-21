# My Rating = 1
# https://leetcode.com/contest/weekly-contest-215/problems/design-an-ordered-stream/

class OrderedStream:

    def __init__(self, n: int):
        self.ptr = 1
        self.rec = {}

    def insert(self, id: int, value: str) -> List[str]:
        self.rec[id]=value
        ret=[]
        while self.ptr in self.rec:
            ret.append(self.rec[self.ptr])
            self.ptr += 1
        return ret


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(id,value)