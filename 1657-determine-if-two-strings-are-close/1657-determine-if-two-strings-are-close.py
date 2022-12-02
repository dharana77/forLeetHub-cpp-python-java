class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # step 1
        if len(word1) != len(word2):
            return False
        
        # step 2
        cnt1, cnt2 = {}, {}

        # step 3
        for c in word1:
            if c in cnt1:
                cnt1[c] += 1
            else:
                cnt1[c] = 1

        # step 4
        for c in word2:
            if c in cnt2:
                cnt2[c] += 1
            else:
                cnt2[c] = 1
        
        word1_cts = sorted(list(cnt1.values()))
        word2_cts = sorted(list(cnt2.values()))
        
        if word1_cts == word2_cts and set(word1) == set(word2):
            return True
        #aabbzccc
        #ccbbazzz
        return False