from __future__ import annotations


class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        max = 0
        for user in accounts:
            wealth = sum(user)
            max = wealth if max < wealth else max
        return max


# memo is not found. happy new year problem