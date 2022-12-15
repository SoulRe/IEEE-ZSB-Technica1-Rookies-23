#it doesn't work in vscode obviously but it does in leetcode
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort(reverse = True)
        #print(stones)
        while len(stones) > 1:
            if stones[0] == stones[1]:
                stones.pop(1)
                stones.pop(0)
                stones.sort(reverse = True) 
                continue
            if stones[0] > stones[1]:
                stones[0] -= stones[1]
                stones.pop(1)
                stones.sort(reverse = True) 
        if len(stones) == 0:
            return 0
        else:
            return stones[0]