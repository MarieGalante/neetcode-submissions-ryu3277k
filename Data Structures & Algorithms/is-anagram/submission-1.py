class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if s[::-1] is t:
        #     return True
        # else:
        #     return False
        # if len(s) is not len(t):
        #     return False

        sdict = {}
        for  i in range(len(s)):
            if s[i] not in sdict:
                sdict[s[i]] = 1
            else:
                sdict[s[i]] += 1

        tdict = {}
        for  i in range(len(t)):
            if t[i] not in tdict:
                tdict[t[i]] = 1
            else:
                tdict[t[i]] += 1


        if sdict == tdict:
            return True
        else:
            return False