#User function Template for python3

class Solution:
    def calc_Sum (self, arr1, arr2) : 
        #Complete the function
        i = len(arr1) - 1
        j = len(arr2) - 1
        carry = 0
        ans = []
        while i >= 0 or j >= 0 or carry:
            d1 = arr1[i] if i >= 0 else 0
            d2 = arr2[j] if j >= 0 else 0
            total = d1 + d2 + carry
            ans.append(str(total % 10))
            carry = total // 10
            i -= 1
            j -= 1

        return ''.join(ans[::-1])