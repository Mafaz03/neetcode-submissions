class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n1 = len(a)
        n2 = len(b)

        if n1 > n2:
            extra = "0" * (n1 - n2) 
            b = extra + b
        
        if n2 > n1:
            extra = "0" * (n2 - n1) 
            a = extra + a
        
        # print(a)
        # print(b)

        n = len(a)

        res = ""

        carry = False
        for i in reversed(range(n)):
            if (not carry) and (a[i] == "0" and b[i] == "0"):
                temp_sum = "0"
                carry = False
            
            elif (not carry) and ((a[i] == "1" and b[i] == "0") or (a[i] == "0" and b[i] == "1")):
                temp_sum = "1"
                carry = False
            
            elif (not carry) and (a[i] == "1" and b[i] == "1"):
                temp_sum = "0"
                carry = True
            
            elif (carry) and (a[i] == "0" and b[i] == "0"):
                temp_sum = "1"
                carry = False
            
            elif (carry) and ((a[i] == "1" and b[i] == "0") or (a[i] == "0" and b[i] == "1")):
                temp_sum = "0"
                carry = True
            
            elif (carry) and (a[i] == "1" and b[i] == "1"):
                temp_sum = "1"
                carry = True
            
            
            res = temp_sum + res

            # print(res)
        if carry:
            res = "1" + res
        return res



            


