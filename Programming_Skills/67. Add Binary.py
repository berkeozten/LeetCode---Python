class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # bin() gives binary
        # int(BinaryVal, 2) gets int val

        return str(bin(int(a,2) + int(b,2)))[2:]


        