class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1)==1:
            if s1 in s2:
                return True
            else:
                return False
        

        if len(s1)>len(s2):
            return False
        
        # need a sliding window of size s1?

        # brute force
        # s2sorted = sorted(s2)
        # print(sorted(s2))
        # print(sorted(s1))
        # print("".join(sorted(s1)))
        teststr = "".join(sorted(s1))
        for r in range(len(s2)-len(s1)+1):
            
            substr = s2[r: r + len(s1)]
            substrsort = "".join(sorted(substr))
            # print(substrsort)
            if teststr in substrsort:
                return True
        
        return False