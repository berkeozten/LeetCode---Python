class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        x,y,z=0,0,0
        for i in bills:
            #print(f"{i = } {x = } {y = } {z = }")
            if i == 5:
                x += 1
            elif i == 10 and x > 0:
                y += 1
                x -= 1
            elif i == 20 and y > 0 and x > 0:
                z += 1
                y -= 1
                x -= 1
            elif i == 20 and x > 2:
                z += 1
                x -= 3
            else:
                return False
        return True
        