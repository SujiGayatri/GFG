class Solution:
    def addFraction(self, num1: int, den1: int, num2: int, den2: int) -> list[int]:
        # code here
        lcm = (den1 * den2) // gcd(den1, den2)
        numerator = num1 * (lcm // den1) + num2 * (lcm // den2)
        g = gcd(numerator, lcm)
        return [numerator // g, lcm // g]