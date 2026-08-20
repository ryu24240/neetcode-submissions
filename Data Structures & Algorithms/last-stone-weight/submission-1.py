import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
             heaviest = -heapq.heappop(max_heap)
             second_heaviest = -heapq.heappop(max_heap)

             k = heaviest - second_heaviest

             if k != 0:
                 heapq.heappush(max_heap, -k)

        return -max_heap[0] if max_heap else 0
