class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        def calWeight(stones: List[int]) -> List[int]:
             if len(stones) == 0:
                return 
             if len(stones) != 1:
                stones.sort(reverse=True)
                heaviest = stones[0]
                secound_heaviest = stones[1]
                k = heaviest - secound_heaviest
                stones.pop(0)
                stones.pop(0)
                stones.append(k)
                calWeight(stones)
             return stones

        final_stone = calWeight(stones)
        return final_stone[0]