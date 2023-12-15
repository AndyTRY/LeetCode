from typing import List
class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        def reducedMat(mat : List[set]) -> List[set]:
            reducedMat = []
            for i in range(len(mat)//2):
                idx = i*2
                reducedSet = {x + y for x in mat[idx] for y in mat[idx + 1]}
                reducedMat.append(reducedSet)
            
            if len(mat) % 2 == 1:   reducedMat.append(mat[-1])
            return reducedMat
        
        for i, lst in enumerate(mat): mat[i] = set(lst)
        while len(mat) != 1:  mat = reducedMat(mat)

        best = float("inf")
        for num in mat[0]:  best = min(abs(target - num), best)

        print(best)
        return best

x  = Solution()
x.minimizeTheDifference([[1],[2],[3]], 100)