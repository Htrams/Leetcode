# My Rating = 2
# https://leetcode.com/explore/featured/card/november-leetcoding-challenge/567/week-4-november-22nd-november-28th/3540/

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        convertor = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        morseCodeRec = set()
        for word in words:
            morseCode = ""
            for letter in word:
                morseCode += convertor[ord(letter) - ord('a')]
            morseCodeRec.add(morseCode)
        return len(morseCodeRec)