# 345. Reverse Vowels of a String

# Example 1:

# Input: s = "hello"
# Output: "holle"
# Example 2:

# Input: s = "leetcode"
# Output: "leotcede"


class Solution:
    def reverseVowels(self, sr: str) -> str:
        s = list(sr)
        vowles = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        l = 0
        r = len(sr) - 1
        while l < r:
            if s[l] not in vowles:
                l += 1

            if s[r] not in vowles:
                r -= 1
            if s[l] in vowles and s[r] in vowles:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
        return "".join(s)
