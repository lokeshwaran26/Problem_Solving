# #### Input 1
# python
# s = "babad"

# *Expected Output:*
# python
# ['bab', 'aba']


# #### Input 2
# python
# s = "cbbd"

# *Expected Output:*
# python
# ['bb']


# #### Input 3
# python
# s = "aabbaa"

# *Expected Output:*
# python
# ['aabbaa', 'abccba', 'bbaa', 'aa']


# ### Test Cases

# #### Test Case 1
# *Input:*
# python
# s = "racecar"

# *Expected Output:*
# python
# ['racecar']


# #### Test Case 2
# *Input:*
# python
# s = "banana"

# *Expected Output:*
# python
# ['anana', 'anana', 'nana', 'ana', 'ana']


# #### Test Case 3
# *Input:*a
# python
# s = "abccba"

# *Expected Output:*
# python
# ['abccba', 'bccb', 'cc']

# s = "banana"
# li = []
# l = 0
# r = 1
# while l < len(s):
#     while r < len(s):
#         sub_str = s[l:r+1]
#         if sub_str == sub_str[::-1]:
#             li.append(sub_str)
#         r+=1
#     r = 0
#     l+=1
#     r = l+1
# print(li)




# s = "babad"
#    ij -- sub_str = "ba" --> "ad"
#    i j   

# ba
# bab
# baba
# babad


s = "abccba"
reversing = []
for i in range(len(s)): # i --> 0 - a --> 1 - b 
    for j in range(i+1, len(s)): # j --> 1 - b
        store = s[i:j+1]   # 
        print(store)
        if store == store[::-1]:
            reversing.append(store)
print(f'Input: {s}' , '\nOutput' ,reversing)