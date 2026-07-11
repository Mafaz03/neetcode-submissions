class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] < 9:
            digits[-1] += 1
            return digits

        digits[-1] = 0
        carry = 1
        for i in range(len(digits)-2, -1, -1):
            if digits[i] + carry >= 10:
                digits[i] = (digits[i] + carry) % 10
                carry = (digits[i] + carry) % 100
            else:
                digits[i] = digits[i] + carry
                carry = 0
        
        if carry != 0:
            digits = [carry] + digits
        return digits