from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 1) loop through list
        # 2) make an id for each string we encounter and store in dictionar
        # 3) seen # id: list[string]
        seen = defaultdict(list)        
        for string in strs:
            count = [0]*26 # initialise id for each string
            # make id
            for s in string:
                count[ord(s) - ord("a")] += 1 
            seen[tuple(count)].append(string)

        # print(list(seen.values()))
        return list(seen.values())