class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left, up, right, down = 0, 0, len(matrix[0]), len(matrix)
        result = []
        while True:
            if left == right or up == down:
                    break
            result += matrix[up][left:right]
            up += 1 
            #print(f"{result} {up} {down}")
            if up >= down:
                break
            else: 
                for i in range(up,down-1):
                    #print(f"here 1: {result}")
                    result.append(matrix[i][right-1])
            
            #print(f"here 2: {result}")
            result += (matrix[down-1][left:right])[::-1]
            right -= 1
            down -= 1
            
            if left == right or up == down:
                    break
            flag = down - 1
            #print(f"{result} {up} {down} {left} {right}")
            while flag >= up:                
                #print(f"here 3: {result}")
                result.append(matrix[flag][left])                    
                flag -= 1
            left += 1
            #print(f"here 4: {result}")

        return result