class Solution:
    def  typeOfArr(self , arr):
        #code here.
        n = len(arr)
        drops = 0
        rises = 0
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                drops += 1
            else:
                rises += 1
        if drops == 0:
            return 1          
        if rises == 0:
            return 2          
        if drops == 1 and arr[-1] < arr[0]:
            return 4          
        return 3