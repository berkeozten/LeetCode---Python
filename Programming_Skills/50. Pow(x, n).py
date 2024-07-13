class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0.0:
            return 0.0
        elif x == 1.0:
            return 1.0
        elif x == -1.0:
            return -1.0 if n % 2 == 1 else 1.0

        return x**n