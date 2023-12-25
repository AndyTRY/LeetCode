from typing import List
from bitarray import bitarray
class Solution:
    def smallestMissingValueSubtree(self, parents: List[int], nums: List[int]) -> List[int]:
        class Node():
            def __init__(self, id, genVal):
                self.id = id
                self.genVal = genVal
                self.children = []
                self.smallests = [None, None]
                self.bitmap = None

        class BitMap():
            def __init__(self, bitmap = None, index = None) -> None:
                if bitmap is not None:
                    self.bitmap = bitmap
                else:
                    bitmap = bitarray(10000 + 1)
                    bitmap.setall(0)
                    self.bitmap = bitmap
                self.freeIndex = index if index is not None else 1

            def setVal(self, val):
                self.bitmap[val] = True
                while self.bitmap[self.freeIndex] == True:
                    self.freeIndex += 1
            
            @classmethod
            def bitwise_or(cls, bitmap1, bitmap2):
                newBitmap = bitmap1.bitmap | bitmap2.bitmap
                freeIndex = max(bitmap1.freeIndex, bitmap2.freeIndex)
                while newBitmap[freeIndex] == True:
                    freeIndex += 1
                return BitMap(newBitmap, freeIndex)
        

        # Build Tree
        getNode = {}
        for i in range(len(nums)):
            getNode[i] = Node(i, nums[i])
        
        for i in range(1,len(parents)):
            node = getNode[i]
            parentNode = getNode[parents[i]]
            parentNode.children.append(node)
        

        output = [-1 for i in range(len(nums))]

        def determineSmallests(node):
            if len(node.children) == 0:
                bitmap = BitMap()
                bitmap.setVal(node.genVal)
                output[node.id] = bitmap.freeIndex

                return bitmap
        
            else:
                bitmap = BitMap()
                for children in node.children:
                    childBitmap = determineSmallests(children)
                    bitmap = BitMap.bitwise_or(bitmap, childBitmap)

                bitmap.setVal(node.genVal)
                output[node.id] = bitmap.freeIndex
                return bitmap
        
        determineSmallests(getNode[0])
        print(output)
        return output



            

        
        

x = Solution()
x.smallestMissingValueSubtree([-1,0,1,0,3,3],[5,4,6,2,1,3])



