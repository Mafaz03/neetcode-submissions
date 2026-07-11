class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1, num2]:
            return "0"

        digit_map = {
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            }

        rev = {v: k for k, v in digit_map.items()}

        amounts = []

        for idx2, d2 in enumerate(reversed(num2)):
            total = 0
            carry = 0
            place = 0

            for d1 in reversed(num1):
                digit = digit_map[d2] * digit_map[d1] + carry

                carry = digit // 10
                res = digit % 10

                total += res * (10 ** place)
                place += 1

            if carry:
                total += carry * (10 ** place)

            total *= 10 ** idx2

            amounts.append(total)

        amount = sum(amounts)

        res = ""
        while amount:
            digit = amount % 10
            res += rev[digit]
            amount = amount // 10

        return res[::-1]
        

           