#User function Template for python3

class Solution:
    def getDayOfWeek(self, d, m, y):
        # code here 
        days = ["Sunday", "Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday"]
        if m < 3:
            m += 12
            y -= 1
        k = y % 100
        j = y // 100
        h = (d + (13 * (m + 1)) // 5 + k + (k // 4) +
             (j // 4) + (5 * j)) % 7
        zeller_days = ["Saturday", "Sunday", "Monday",
                       "Tuesday", "Wednesday", "Thursday", "Friday"]

        return zeller_days[h]