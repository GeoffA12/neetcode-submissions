class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        for i in range(1, n):
            temp = two
            two = one + two
            one = temp
        
        return two