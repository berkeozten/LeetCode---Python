class Solution:
    def judgeCircle(self, moves: str) -> bool:
        xyArr = [0,0]
        for elem in moves:
            if elem == 'U':
                xyArr[0] += 1
            elif elem == 'D':
                xyArr[0] -= 1
            elif elem == 'R':
                xyArr[1] += 1
            else:
                xyArr[1] -= 1
        return xyArr == [0,0]