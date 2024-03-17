class Solution:
    def sortColors(self, nums: List[int]) -> None:
        sorted = False
        while not sorted:
            sorted = True
            for i in range(len(nums)-1):
                if nums[i] > nums[i+1]:
                    sorted = False
                    nums[i], nums[i+1] = nums[i+1], nums[i]
        return nums



        """
        Do not return anything, modify nums in-place instead.
        """
        