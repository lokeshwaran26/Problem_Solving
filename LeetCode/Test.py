# 345. Reverse Vowels of a String

# Example 1:

# Input: s = "hello"
# Output: "holle"
# Example 2:

# Input: s = "leetcode"
# Output: "leotcede"

def convert_vowels(s):
    vowles = ['a','e','i','o','u','A','E','I','O','U']
    sc = 'abcbnim'
    m = list(sc)
    print(m)
    sr = list(s)
    print(sr)
    l = 0
    r = len(sr) -1
    while l < r:
        if sr[l] in vowles and sr[r] in vowles:
            sr[l],sr[r] = s[r],s[l]
            l+=1
            r-=1
        if s[l] not in vowles:
            l+=1
        if s[r] not in vowles:
            r-=1
    return ''.join(sr) 

print(convert_vowels('hello'))
    