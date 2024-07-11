class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        total = 0
        for i in range(len(mat)):
            total += mat[i][i]

        print(total)

        for i in range(len(mat)):
            total += mat[len(mat) - i - 1][i]

        if len(mat) % 2 != 1:        
            return total
        else:
            return total - mat[len(mat)//2][len(mat)//2]