# My Rating = 1
# https://leetcode.com/contest/weekly-contest-220/problems/reformat-phone-number/


class Solution:
    def reformatNumber(self, number: str) -> str:
        count=0
        output=''
        numbers=[]
        for num in number:
            if num==' ' or num=='-':
                continue
            numbers.append(num)
            count+=1
        i=0
        while count>4:
            output=output+numbers[i]+numbers[i+1]+numbers[i+2]
            output=output+'-'
            i+=3
            count-=3
        if count==4:
            output=output+numbers[i]+numbers[i+1]+'-'+numbers[i+2]+numbers[i+3]
        elif count==3:
            output=output+numbers[i]+numbers[i+1]+numbers[i+2]
        elif count==2:
            output=output+numbers[i]+numbers[i+1]
        return output