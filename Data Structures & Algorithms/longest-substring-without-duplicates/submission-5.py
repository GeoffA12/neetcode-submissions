class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        l = list(s)
        uniqueCharacters = set()
        right = 0
        left = 0

        while left < len(l) and right < len(l):
            if l[right] not in uniqueCharacters:
                uniqueCharacters.add(l[right])
                right += 1
            else:
                length = right - left
                if length > maxLength:
                    maxLength = length
                
                uniqueCharacters.remove(l[left])
                left += 1
                # while left < right:
                #     left += 1
                #     if l[left] != l[right]:
                #         break
                #     else:
                #         uniqueCharacters.remove(l[left])
                    
            
        return max(len(uniqueCharacters), maxLength)


        # ptr = 0
        # while ptr < len(l):
        #     if l[ptr] not in uniqueCharacters:
        #         uniqueCharacters[l[ptr]] = ptr
        #         ptr += 1
        #     else:
        #         repeatedChar = l[ptr]
        #         originalIdx = uniqueCharacters[l[ptr]]
        #         length = ptr - originalIdx

        #         if length > maxLength:
        #             maxLength = length
                
        #         if ptr - originalIdx > 1:
        #             ptr = originalIdx + 1
        #         else:
        #             ptr = ptr
        #         uniqueCharacters.clear()
            
    
        # return max(len(uniqueCharacters), maxLength)