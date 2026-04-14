class Solution:

    def encode(self, strs: List[str]) -> str:
        # total_len = 0
        # for i in range(len(strs)):
        #     total_len += len(strs[i])
        encoded_string = ""
        for i in range(len(strs)):
            encoded_string += str(len(strs[i])) + "#" + strs[i]

        return encoded_string 

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            j = s.find("#", i)
            wordlen = int(s[i:j])
            strs.append(s[j + 1 : j + 1 + wordlen])
            i = j + 1 + wordlen
        return strs