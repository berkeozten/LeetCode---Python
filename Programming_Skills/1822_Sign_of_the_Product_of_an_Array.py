class Solution:
    def arraySign(self, nums: List[int]) -> int:
        lastSign: int = 1
        for n in nums:
            if n == 0:
                return 0
            elif n < 0:
                lastSign = lastSign * -1

        return lastSign
        