class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        Xlist = [ False for k in range(len(matrix))]
        Ylist = [ False for k in range(len(matrix[0]))]

        for i in range(len(Xlist)):
            for j in range(len(Ylist)):
                    if matrix[i][j] == 0:
                        Xlist[i] = True
                        Ylist[j] = True
                
        #print(Xlist)
        #print(Ylist)

        for i in range(len(Xlist)):
            for j in range(len(Ylist)):
                if Xlist[i] or Ylist[j]:
                    matrix[i][j] = 0

        
                    