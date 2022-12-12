from __future__ import annotations


class Solution:
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        # mat to the list of number 1
        soldiers: dict[int, int] = {}
        for i, row in enumerate(mat):
            soldiers[i] = sum(row)
        sorted_rows = dict(sorted(soldiers.items(), key=lambda x: x[1]))
        return list(sorted_rows.keys())[:k]

# memo
# binary search (二分探索)
    def binarySearch(
        self,
        mat: list[list[int]],
        k: int
    ) -> list[int]:
        n = len(mat[0])
        for row in mat:
            low = 0
            high = n
            while low < high:
                mid = (high + low) // 2
                if row[mid] == 1:
                    low = mid + 1
                else:
                    high = mid
            return low


# priority queue: this is heapqueue, heapq
# heap is suitable structure for estimating minimum or maximum number
# heap[0] is the minimum number, so if you want to remove maximum one, you should multiply by -1 and then reverse the order
