# Scenario: Largest Product of Subarrays

# # Problem Statement

# You are given a list of integers, and you need to find the largest product of any contiguous subarray. A contiguous subarray is a sequence of consecutive elements from the list.

# Write a function max_product_subarray(nums) that takes a list of integers nums and returns the largest product that can be obtained from any contiguous subarray.

# # Sample Input and Expected Output

# # Input 1
# python
# nums = [2, 3, -2, 4]

# *Expected Output: * 
# python
# 6


# # Input 2
# python
# nums = [-2, 0, -1]

# *Expected Output: *
# python
# 0


# # Input 3
# python
# nums = [-2, -3, 0, -2, -40]

# *Expected Output: *
# python
# 80


# # Test Cases

# # Test Case 1
# *Input: *
# python
# nums = [1, -2, -3, 4]

# *Expected Output: *
# python
# 24


# # Test Case 2
# *Input: *
# python
# nums = [0, -1, -2, 0]

# *Expected Output: *
# python
# 0


# # Test Case 3
# *Input: *
# python
# nums = [2, -5, -2, -4, 3]

# *Expected Output: *
# python
# 240


# # Function Signature

# python

# # Input 3
# python
# nums = [-2, -3, 0, -2, -40]

# *Expected Output: *
# python
# 80



    # Your code here
# nums = [-2, 0, -1]
# nums = [-2, -3, 0, -2, -40]
# # nums = [-2, -3, 0, -2, -40]
#         #   l   r
# # i - 0 -- >
# l = 0
# r = 1
# #li = []
# li = []
# for i in range(len(nums)-1):
#     li.append(nums[l]*nums[r])
#     l+=1
#     r+=1
# print(max(li))
# print(li)




nums = [ 5,5,1,1,2,2,4]
nums.sort()
n = len(nums)
if n == 1:
    print(nums[0])

temp = 1
while temp < n:
    if  nums[temp-1] != nums[temp]:
       print( nums[temp-1])
    temp += 2    
#  print(nums[temp-1])


