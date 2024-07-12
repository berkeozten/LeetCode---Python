class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums = sorted(nums, reverse = True)

        for ix in range(len(nums) - 2):
            if nums[ix + 2] + nums[ix + 1] > nums[ix]:
                return nums[ix + 2] + nums[ix + 1] + nums[ix]

        return 0