class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        if bills[0] != 5: return False
        
        absolute_change_available = 0
        change_avaiable = {5: 0, 10: 0, 20: 0}

        for b in bills:
            change_avaiable[b] += 1
            print("before: ", change_avaiable)

            change = b - 5
            
            if change:
                if change == 5:
                    if change_avaiable[5]:
                        change_avaiable[5] -= 1
                    else:
                        return False
                
                if change == 15:
                    if ((change_avaiable[10]) and (change_avaiable[5] >= 1)):
                        change_avaiable[10] -= 1
                        change_avaiable[5]  -= 1
                    
                    elif (change_avaiable[5] >= 3):
                        change_avaiable[5] -= 3
                    
                    else: return False
            print("after: ", change_avaiable)
            print("\n")
        return True
            

