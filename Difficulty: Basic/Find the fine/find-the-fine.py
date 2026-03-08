#User function Template for python3

class Solution:
    def totalFine(self, date, car, fine):
        #Code here
        total = 0
        for i in range(len(car)):
            if date % 2 == 0:  
                if car[i] % 2 == 1:  
                    total += fine[i]
            else:  
                if car[i] % 2 == 0: 
                    total += fine[i]
        return total
    
    
    