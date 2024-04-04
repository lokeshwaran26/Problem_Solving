# 151. Reverse Words in a String

# Example 1:

# Input: s = "the sky is blue"
# Output: "blue is sky the"
# Example 2:

# Input: s = "  hello world  "
# Output: "world hello"
# Explanation: Your reversed string should not contain leading or trailing spaces.
# Example 3:

# Input: s = "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.


class Solution:
    def reverseWords(self, s: str) -> str:
        li = s.split()
        res = ' '.join(li[::-1])
        # res = ''
        # for item in li[::-1]:
        #     res = res + item + " "

        return res.strip()
