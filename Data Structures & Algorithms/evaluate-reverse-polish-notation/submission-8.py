class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # go from bottom to top of stack
        # popping as we go
        if len(tokens) == 1: return int(tokens[0])
        i = 0
        opls = ["*", "/", "+", "-"]
        while len(tokens)>1:
            print(i)
            print(tokens)
            if tokens[i] in opls:
                if "+" == tokens[i]:
                    res = int(tokens[i-2]) + int(tokens[i-1])
                elif "-" == tokens[i]:
                    res = int(tokens[i-2]) - int(tokens[i-1])
                elif "/" == tokens[i]:
                    res = int(int(tokens[i-2]) / int(tokens[i-1]))
                elif "*" == tokens[i]:
                    res = int(tokens[i-2]) * int(tokens[i-1])
                
                tokens[i] = str(res)
                tokens.pop(i-1)
                tokens.pop(i-2)
                i -= 1
            else:
                i += 1

        return int(tokens[0])