from __future__ import annotations


class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        out = []
        for num in range(1, n+1):
            if num % 3 == 0 and num % 5 == 0:
                out.append("FizzBuzz")
            elif num % 5 == 0:
                out.append("Buzz")
            elif num % 3 == 0:
                out.append("Fizz")
            else:
                out.append(str(num))
        return out


# memo append Fizz and Buzz different timing