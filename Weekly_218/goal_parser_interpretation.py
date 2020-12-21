# My Rating = 1
# https://leetcode.com/contest/weekly-contest-218/problems/goal-parser-interpretation/

# You own a Goal Parser that can interpret a string command. The command consists of an alphabet 
# of "G", "()" and/or "(al)" in some order. The Goal Parser will interpret "G" as the 
# string "G", "()" as the string "o", and "(al)" as the string "al". The interpreted strings are then 
# concatenated in the original order.
# Given the string command, return the Goal Parser's interpretation of command.

class Solution:
    def interpret(self, command: str) -> str:
        output = ""
        i=0
        leng=len(command)
        while i<leng:
            if command[i]=='G':
                output = output + 'G'
                i += 1
            elif command[i]=='(' and command[i+1]==')':
                output = output + 'o'
                i += 2
            else:
                output = output + 'al'
                i += 4
        return output