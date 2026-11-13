"""
Start at index 1
[b]
push b into the queue.
pop it. 
Look to the left and right index (0, 2)
If the left index is out of bounds, compare the current index to the right index. If the right index is out of bounds, compare the current index to the left index. If there is no left or right index, add the index to the result array
are s[0] == s[2] equal? 
If not, do not push anything into the queue. Move to the next index
Push a into the queue. Add it's index into a result array that tracks the substring with the largest palindrome [2]
Look to the left and right index (1, 3)
Is s[1] == s[3]? Yes
Push 1, 3 onto the queue
Iterate over 1 and 3 in the queue (the full length of the queue). Add s[index] to the result array
Are the letters to the left and right of 1 equal to each other? No ('a' != 'd') for index 3. 
Are the value 
"""

"""
Start in the middle. 

Continue this loop until either the left side is at the edge or the right side is at the edge. 

Assign left to the middle index, right to the middle as well. If it's an even array, compare the two innermost indices. 

If the values are equal push the letter(s) to a stack. Move left and move right. 
The palindrome will be the letters on the stack.

If the both the left and right values are unequal and the stack is empty, there is no need to continue, a palindrome wasn't found. Exit the loop. 

Peek the top of the stack if there are values in it. If one of the values is equal to either left or right pointer, then move just that one pointer and add the the unequal pointer to the stack. Keep the unequal pointer that isn't equal to the previous top of the stack in it's current position. 

Once you moved left or right (individually), check if the next position equals the top of the stack. If not, then pop the top of the stack and return the palindrome that was formed in the stack. 

"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = list(s)
        if len(l) == 1:
            return l[0]

        def palindrome(left, right):
            word = ''
            while left >= 0 and right < len(l):
                if l[left] == l[right]:
                    if left == right:
                        word = l[left]
                    else:
                        word = l[left] + word + l[right]
                    left -= 1
                    right += 1
                else:
                    break
                    
            return word

        palindromes = []

        for i in range(len(l) - 1):
            p = palindrome(i, i)
            p1 = palindrome(i, i+1)
            palindromes.append(p)
            palindromes.append(p1)

        return max(palindromes, key=len)



            
                    






                
