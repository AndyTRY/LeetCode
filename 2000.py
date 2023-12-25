class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        def InplaceReverse(s, t):
            tlen = t - s + 1
            for i in range((tlen//2)):
                temp = word[s]
                word[s] = word[t]
                word[t] = temp
                s+=1
                t+=1
            
        
        for i in range(len(word)):
            if word[i] == ch:
                InplaceReverse(0, i)
                return word
        
        return word
        
