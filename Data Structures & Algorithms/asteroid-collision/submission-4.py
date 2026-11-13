"""
2 pointer approach
* Keep a left and right pointer to compare asteroids
* left starts at a[0] and right starts at a[1]
* If the asteroids are moving in the same direction, advance l and r
* If the asteroids are moving in opposite directions, 2 things can happen
1. there's an explosion and they both explode(equal absolute value)
2. one asteroid crashes with the other, and the smaller one explodes

In case 1, the left and right pointers need to move, because the 2 asteroids were destroyed. 
- move left back one index
- move right up one index
In case 2, the smaller asteroid was destroyed. If the asteroid at left pointer was destroyed, move the left pointer back one index. If the asteroid at the right pointer is destroyed, move the right pointer up one index. 
Continue this loop until right exceeds the length of the asteroids array
"""

# [2, 4, -4, -1]
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        left = 0
        right = 1
        answer = asteroids.copy()

        while right < len(answer) and left >= 0:
            asteroid1 = answer[left]
            asteroid2 = answer[right]

            if (asteroid1 > 0 and asteroid2 > 0) or (asteroid1 < 0 and asteroid2 < 0):
                left += 1
                right += 1
                continue
            
            # Collisions only happen when a positive bound asteroid is to the left or a negative bound asteroid 
            if asteroid1 > 0 and asteroid2 < 0:
                if abs(asteroid1) > abs(asteroid2):
                    answer.pop(right)
                
                if abs(asteroid2) > abs(asteroid1):
                    answer.pop(left)
                    if left > 0:
                        left -= 1
                        right -= 1
                
                if abs(asteroid1) == abs(asteroid2):
                    answer.pop(right)
                    answer.pop(left)
                    if left > 0:
                        left -= 1
                        right -= 1
            else:
                left += 1
                right += 1
        
        return answer
            


        