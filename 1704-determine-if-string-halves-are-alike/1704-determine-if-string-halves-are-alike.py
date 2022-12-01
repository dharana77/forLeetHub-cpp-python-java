class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        import re

        # Split the string into two halves
        a = s[:len(s) // 2]
        b = s[len(s) // 2:]

        # Count the number of vowels in each half using a regular expression
        countVowels = lambda str: len(re.findall(r'[aeiouAEIOU]', str))
        countVowelsInA = countVowels(a)
        countVowelsInB = countVowels(b)

        # Return True if the number of vowels in each half is equal, and False otherwise
        return countVowelsInA == countVowelsInB