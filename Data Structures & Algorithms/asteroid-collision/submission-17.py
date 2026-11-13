class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        stack.append(asteroids[0])

        answer = []
        ptr = 1
        while ptr < len(asteroids):
            # print(stack)
            asteroid = asteroids[ptr]
            if len(stack) == 0:
                asteroidNeighbor = asteroid
            else:
                asteroidNeighbor = stack[-1]

            # Asteroids moving in the same direction won't collide
            if (asteroid > 0 and asteroidNeighbor > 0) or (asteroid < 0 and asteroidNeighbor < 0):
                stack.append(asteroid)
                ptr += 1
            
            # Asteroids moving in opposite directions won't collide
            if asteroidNeighbor < 0 and asteroid > 0:
                stack.append(asteroid)
                ptr += 1
            

            # Collision
            if asteroidNeighbor > 0 and asteroid < 0:
                if abs(asteroid) == abs(asteroidNeighbor):
                    # Both the neighboring asteroid is deleted, and the current asteroid is not added to the stack.
                    stack.pop()
                    ptr += 1
                    continue
                
                if abs(asteroidNeighbor) > abs(asteroid):
                    ptr += 1
                    continue
                
                while asteroidNeighbor > 0 and (abs(asteroid) > abs(asteroidNeighbor)):
                    stack.pop()
                    if len(stack) > 0:
                        asteroidNeighbor = stack[-1]
                    else:
                        asteroidNeighbor = asteroid
                    
                if len(stack) == 0:
                    stack.append(asteroid)
                else:
                    if (asteroidNeighbor > 0):
                        # We know that the the asteroidNeighbor is bigger than or equal to the asteroid.
                        # We're working with different signs, so we need to figure out if they're equal or the value in the stack is bigger than the asteroid
                        # I think this needs to be in a while loop?
                        if abs(asteroidNeighbor) == abs(asteroid):
                            stack.pop()
                        else:
                            pass
                            # The asteroidNeighbor is bigger than the asteroid, so we don't need to do anything.
                    else:
                        # The asteroid neighbor and the asteroid are negative. Can safely append to the stack
                        stack.append(asteroid)
                
                ptr += 1

        
        return stack
                    
                

