nums = [5, 5, 1, 1, 2, 2, 4]
nums.sort()
n = len(nums)
if n == 1:
    print(nums[0])

temp = 1
while temp < n:
    if nums[temp-1] != nums[temp]:
       print(nums[temp-1])
    temp += 2
#  print(nums[temp-1])
