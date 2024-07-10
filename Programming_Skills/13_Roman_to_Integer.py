class Solution:
    def romanToInt(self, s: str) -> int:
        dictRoman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        result = 0
        lastVal = 0
        for c in s:
            result += dictRoman[c]

            if dictRoman[c] > lastVal:
                result -= 2*lastVal
                                
            lastVal = dictRoman[c]

        return result


        