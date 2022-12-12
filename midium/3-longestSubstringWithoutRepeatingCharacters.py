from collections import deque


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = deque()
        maxLength = 0
        for char in s:
            if char in sub:
                if (maxSubLen := len(sub)) > maxLength:
                    maxLength = maxSubLen
                c = ""
                # popleft until same character is removed
                while c != char:
                    c = sub.popleft()
            sub.append(char)
        if (maxSubLen := len(sub)) > maxLength:
            maxLength = maxSubLen
        return maxLength
