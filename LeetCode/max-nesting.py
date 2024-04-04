# Maximum Nesting Depth of the Parentheses


# Example 1:

# Input: s = "(1+(2*3)+((8)/4))+1"
# Output: 3
# Explanation: Digit 8 is inside of 3 nested parentheses in the string.
# Example 2:

# Input: s = "(1)+((2))+(((3)))"
# Output: 3


class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        max_count = 0
        for i in s:
            if i == '(':
                count += 1
                if max_count < count:
                    max_count = count
            if i == ')':
                count -= 1
        return max_count
