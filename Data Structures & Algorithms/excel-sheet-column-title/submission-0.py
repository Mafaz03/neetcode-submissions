class Solution:

    def convertToTitle(self, columnNumber: int) -> str:
        result = ""

        hash = {i: chr(65+i) for i in range(26)}
        print(hash)

        dummy = columnNumber 
        while dummy:
            res = (dummy - 1) % 26
            result = hash[res] + result

            dummy = (dummy - 1) // 26
        return result
