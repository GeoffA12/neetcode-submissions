class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 1
        l = list(s)
        contained = set()
        if len(l) == 0:
            return 0
        
        length = 0
        maxLength = 0
        contained.add(l[0])
        while right < len(l) and left < len(l):
            left_ch, right_ch = l[left], l[right]
            
            if left_ch == right_ch:
                if left == right:
                    right += 1
                    contained.add(right_ch)
                else:
                    length = right - left
                    if length > maxLength:
                        maxLength = length
                    left += 1
                    if left_ch in contained:
                        contained.remove(left_ch)
                continue

            if right_ch in contained:
                length = right - left
                if length > maxLength:
                    maxLength = length
                if left_ch != right_ch:
                    if left_ch in contained:
                        contained.remove(left_ch)
                left += 1
            else:
                right += 1
            
            contained.add(right_ch)
            
        return max(len(contained), maxLength)