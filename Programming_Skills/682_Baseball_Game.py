class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # operations[i] is "C", "D", "+", or a string representing an integer in the range [-3 * 104, 3 * 104].
        # .insert(ind,val)
        
        i=0
        while i < len(operations):
            if operations[i] == "+":
                operations[i] = operations[i - 1] + operations[i - 2]
            elif operations[i] == "D":
                operations[i] = operations[i - 1] * 2
            elif operations[i] == "C":
                del operations[i]
                del operations[i-1]
                i = i - 2 
            else:
                operations[i] = int(operations[i])

            i += 1

        return sum(operations)        