class Solution:
    def trap(self, height: List[int]) -> int:
        # find prefix max

        prefixmax = [0]*len(height)
        for i in range(1, len(height)):
            if prefixmax[i-1] > height[i-1]:
                prefixmax[i] = prefixmax[i-1]
            else:
                prefixmax[i] = height[i-1]

        suffixmax = [0]*len(height)
        for i in range(len(height)-2, 0, -1):
            if suffixmax[i+1] > height[i+1]:
                suffixmax[i] = suffixmax[i+1]
            else:
                suffixmax[i] = height[i+1]

        print(prefixmax)
        print(suffixmax)
        # now loop through this array to find the water in a given column
        vol = 0
        for i in range(1, len(height)-1):
            vol += max(min(prefixmax[i], suffixmax[i])-height[i], 0)

        return vol
