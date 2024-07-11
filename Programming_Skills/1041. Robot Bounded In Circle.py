class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        mvVector = [(0,1),(1,0),(0,-1),(-1,0)] # U R D L
        x,y = 0,0 
        curVerInd = 0
        
        for i in range(4):
            for elem in instructions:
                if elem == "G":
                    x += mvVector[curVerInd][0]
                    y += mvVector[curVerInd][1]
                elif elem == "R":
                    curVerInd = (curVerInd + 1) % 4
                    curVer = mvVector[curVerInd]
                else:
                    curVerInd = (curVerInd - 1) % 4
                    curVer = mvVector[curVerInd]

            if x == 0 and y == 0:
                return True
        
        return False
