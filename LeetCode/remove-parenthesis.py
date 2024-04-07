# 1249. Minimum Remove to Make Valid Parentheses


# Example 1:

# Input: s = "lee(t(c)o)de)"
# Output: "lee(t(c)o)de"
# Explanation: "lee(t(co)de)", "lee(t(c)ode)" would also be accepted.
# Example 2:

# Input: s = "a)b(c)d"
# Output: "ab(c)d"
# Example 3:

# Input: s = "))(("
# Output: ""
# Explanation: An empty string is also valid.


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []  # Keep track of valid characters.
        array = list(s)

        paranthesisCount = 0  # Number of open parentheses.

        for char in array:
            if char == '(':
                paranthesisCount += 1
                stack.append(char)
            elif char == ')':

                if paranthesisCount > 0:

                    paranthesisCount -= 1
                    stack.append(char)
                else:
                    continue
            else:

                stack.append(char)

        for i in range(len(stack)-1, -1, -1):
            if paranthesisCount > 0 and stack[i] == '(':
                stack.pop(i)
                paranthesisCount -= 1

        return ''.join(stack)


