class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        first = "".join(i for i in word1)
        second = "".join(i for i in word2)
        return first == second