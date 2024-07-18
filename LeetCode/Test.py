# def largestRectangleArea ( heights):
#     maxArea = 0
#     stack = [ ] # pair: (index, height)
#     for i, h in enumerate (heights):
#         start = i
#         while stack and stack [-1][1] > h:
#             index, height = stack.pop()
#             maxArea = max(maxArea, height * (i - index))
#             start = index
#         stack.append((start, h))
#     for i, h in stack:
#         maxArea = max(maxArea, h * (len(heights) - i))
#     return maxArea

# print(largestRectangleArea([2, 1,5,6,2,3]))

# n = [5,8,3,7,9,1]
# m = len(n)
# print(n[1:] + n[:1])
li = "0000000000000000000000000000000000000"
print(len(li))
