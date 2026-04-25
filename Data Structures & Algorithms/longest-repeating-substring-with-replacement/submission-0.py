from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # seen = set(s)

        # numoccur = defaultdict(int) # str:  int
        # for c in s:
        #     numoccur[c] += 1

        # numtostr = defaultdict(list)
        # for key in seen:
        #     numtostr[numoccur[key]].append(key)            

        # for i in range(len(s) - 1, 0, -1):
        #     if len(numtostr[i])>0:
        #         maxoccur = i
        #         break
        
        # repl = numtostr[i][0]
        # # print(maxoccur)
        # # Now we wanna slide the window to replace
        count = {}
        res = 0        
        l, r = 0, 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)

            while r - l + 1 - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res

            
