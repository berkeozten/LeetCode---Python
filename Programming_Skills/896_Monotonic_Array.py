class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        if nums[0] >= nums[-1]: #Decreasing
            for i in range(0,len(nums)-1):
                if nums[i] < nums[i+1]:
                    break
                elif i == len(nums)-2:
                    return True

        else: #Increasing
            for i in range(0,len(nums)-1):
                if nums[i] > nums[i+1]:
                    break
                elif i == len(nums)-2:
                    return True
                
        return False

        