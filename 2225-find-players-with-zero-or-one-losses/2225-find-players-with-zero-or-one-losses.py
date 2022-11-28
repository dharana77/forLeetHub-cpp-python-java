class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        #answer[0] 은 어떤 매치해서도 지지 않은 모든 플레이어 리스트
        #answer[1]는 하나의 매치에서만 진 선수들 리스트
        answer = list()
        from collections import defaultdict
        wins = defaultdict(int)
        loses = defaultdict(int)
        players = set()
        for m in matches:
            winner, loser = m[0], m[1]
            wins[winner]+=1
            loses[loser]+=1
            players.add(winner)
            players.add(loser)
        
        players = list(players)
        never_lost = list()
        only_one_lost = list()
        for i in players:
            if loses[i] == 0:
                never_lost.append(i)
            elif loses[i] == 1:
                only_one_lost.append(i)
        never_lost.sort()
        only_one_lost.sort()
        answer.append(never_lost)
        answer.append(only_one_lost)
        return answer