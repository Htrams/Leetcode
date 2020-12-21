# My Rating = 8
# https://leetcode.com/problems/word-ladder/

from collections import defaultdict
from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList.append(beginWord)
        wordLen = len(beginWord)
        listLen = len(wordList)
        
        # The commented out code, can be used instead of 'get adj of currentWord' but it is slightly slower.
        # for i in range(listLen):
        #     for j in range(i+1,listLen):
        #         letterDiffCount=0
        #         for letterIndex in range(wordLen):
        #             if wordList[i][letterIndex] != wordList[j][letterIndex]:
        #                 letterDiffCount += 1
        #             if letterDiffCount > 1:
        #                 break
        #         if letterDiffCount==1:
        #             adj[i].append(j)
        #             adj[j].append(i)
        
        frontier = deque()
        frontier.append(listLen-1)
        level={listLen-1:0}
        while frontier:
            currentWord = frontier.popleft()
            
            
            # get adj of currentWord
            tempAdj=[]
            for i in range(listLen):
                if i==currentWord or i in level:
                    continue
                letterDiffCount=0
                for letterIndex in range(wordLen):
                    if wordList[currentWord][letterIndex] != wordList[i][letterIndex]:
                        letterDiffCount += 1
                    if letterDiffCount > 1:
                        break
                if letterDiffCount == 1:
                    tempAdj.append(i)
                    
                    
            # for possWord in adj[currentWord]:
            for possWord in tempAdj:
                if possWord not in level:
                    level[possWord] = level[currentWord]+1
                    frontier.append(possWord)
                    if wordList[possWord] == endWord:
                        return level[possWord]+1
        return 0