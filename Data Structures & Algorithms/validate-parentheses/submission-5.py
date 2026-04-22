class Solution:
    def isValid(self, s: str) -> bool:
        # need dictionary of paranthese type, to a list ?
        # mydict = dict[str, list]
        # mylist = []
        # # loop through s
        # mylist.append(s[0])

        if len(s)==1:
            return False

        closingls = [")", "}", "]"]
        openls = ["(", "{", "["]
        closetoopen = {")": "(", "}": "{", "]": "["}
        # for i in range(1, len(s)):
        #     # print(mylist)
        #     if s[i] in closingls:
        #         # check if appropriate opening bracket
        #         if len(mylist)>0:
        #             if mylist[-1] == opening[s[i]]:
        #                 mylist.pop()
        #                 # pop the matching opening
        #             else:
        #                 return False
        #         else: 
        #             return False
        #     else:           
        #         mylist.append(s[i])
        #     # print(mylist[-1])
        #     # print(" ")
        # if len(mylist)==0:
        #     return True
        # else:
        #     return False

        stack = []
        for bracket in s:
            if bracket in openls:
                stack.append(bracket)
            elif stack and closetoopen[bracket] == stack[-1]:
                stack.pop()
            else:
                return False

        if len(stack)==0:
            return True
        else: 
            return False
