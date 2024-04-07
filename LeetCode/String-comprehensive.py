# 443. String Compression


# Example 1:

# Input: chars = ["a", "a", "b", "b", "c", "c", "c"]
# Output: Return 6, and the first 6 characters of the input array should be: ["a", "2", "b", "2", "c", "3"]
# Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
# Example 2:

# Input: chars = ["a"]
# Output: Return 1, and the first character of the input array should be: ["a"]
# Explanation: The only group is "a", which remains uncompressed since it's a single character.
# Example 3:

# Input: chars = ["a", "b", "b", "b", "b",
#                 "b", "b", "b", "b", "b", "b", "b", "b"]
# Output: Return 4, and the first 4 characters of the input array should be: ["a", "b", "1", "2"].
# Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".


class Solution:
    def compress(self, chars: List[str]) -> int:
        cnt = 1
        j = 0

        if len(chars) == 1:
            return 1

        for i in range(1, len(chars) + 1):
            if i < len(chars) and chars[i] == chars[i - 1]:
                cnt += 1
            else:
                chars[j] = chars[i - 1]
                j += 1

                if cnt > 1:
                    for digit in str(cnt):
                        chars[j] = digit
                        j += 1
                cnt = 1

        return j
