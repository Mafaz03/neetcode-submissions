class Solution:
    def romanToInt(self, s: str) -> int:
        hash = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        subtractable = {
            "I": set(["V", "X"]), 
            "X": set(["L", "C"]), 
            "C": set(["D", "M"])
            }
        
        total = 0
        n = len(s)

        for i, r in enumerate(s):
            
            if (i != n-1) and (r in subtractable) and (s[i+1] in subtractable[r]):
                total -= hash[r]
            else:
                total += hash[r]
        return total
