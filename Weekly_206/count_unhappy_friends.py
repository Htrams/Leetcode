# My Rating = 3
# Note this a brute force solution, there are no better algorithms that work faster given the constraints.
# https://leetcode.com/contest/weekly-contest-206/problems/count-unhappy-friends/

# You are given a list of preferences for n friends, where n is always even.
# For each person i, preferences[i] contains a list of friends sorted in the order of preference. In other words, a friend earlier in the list is more preferred than a friend later in the list. Friends in each list are denoted by integers from 0 to n-1.
# All the friends are divided into pairs. The pairings are given in a list pairs, where pairs[i] = [xi, yi] denotes xi is paired with yi and yi is paired with xi.
# However, this pairing may cause some of the friends to be unhappy. A friend x is unhappy if x is paired with y and there exists a friend u who is paired with v but:
# x prefers u over y, and
# u prefers x over v.
# Return the number of unhappy friends.

class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        
        #Better Way to Store the pairs information  O(n)
        pairRec={}
        for i in range(n//2):
            for j in range(2):
                pairRec[pairs[i][j]]=pairs[i][abs(j-1)]
        
        unhappyFriendsCount=0
        for i in range(n//2):
            for j in range(2):
                person=pairs[i][j]
                for k in preferences[person]:
                    if k==pairRec[person]:
                        break
                    flag=0
                    for l in preferences[k]:
                        if l==pairRec[k]:
                            break
                        if l==person:
                            flag=1
                            break
                    if flag==1:
                        unhappyFriendsCount += 1
                        break
        return unhappyFriendsCount