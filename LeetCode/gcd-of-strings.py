class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        a = len(str1)
        b = len(str2)
        if str1 + str2 != str2 + str1:
            return ""
        while b:
            a, b = b, a % b

        maxi = max(str1, str2)
        return maxi[:a]
