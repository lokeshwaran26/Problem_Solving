class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, 1
        while right < len(nums):
            if not nums[left] and nums[right]:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            elif nums[left]:
                left += 1
            right += 1
