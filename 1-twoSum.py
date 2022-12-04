from __future__ import annotations
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        while len(nums) >= 2:
            # target = i*2のときに自身を選ばないようにpopする必要がある＆速い
            i = nums.pop()
            sub = target - i
            if sub in nums:
                return [nums.index(sub), len(nums)]
