class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # freq = defaultdict(list)
        seen = defaultdict(int) # number: occurences
        for el in range(len(nums)):
            seen[nums[el]] += 1

        # now we need to invert the list so we get frequency as the key

        freq = defaultdict(list) # occurences: list(nums)
        # [freq[seen[key]].append(key) for key in seen.keys() ]
        for key in seen:
            freq[seen[key]].append(key)

        res = []
        # For each frequency
        for i in range(len(nums), 0, -1):
            # For all the numbers with that frequency
            for j in range(len(freq[i])):
                res.append(freq[i][j])
            
                if len(res)==k:
                    print(freq)
                    return res
