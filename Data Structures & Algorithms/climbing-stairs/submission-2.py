"""
Start at n-1, and move downwards until you hit 0. 
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        def solutions(t, sums, total_ways, cache):
            if sums == t:
                return 1

            if sums < t:
                if (sums+1) not in cache:
                    one = solutions(t, sums + 1, total_ways, cache)
                    cache[sums+1] = one
                else:
                    one = cache[sums+1]
                
                if (sums+2) not in cache:
                    two = solutions(t, sums + 2, total_ways, cache)
                    cache[sums+2] = two
                else:
                    two = cache[sums+2]
                # [where sums=2, total_ways=1. Where sums=1, one=1, two=1, total_ways = 2, Where sums=0, one=]
                total_ways = (one + two)
            
            if sums > t:
                return 0

            return total_ways 
        
        # dp = 0

        #for i in range(2, n + 1):
        next_answer = solutions(n, 0, 0, {})
            # print(next_answer)
           #c dp = next_answer
        
        return next_answer
