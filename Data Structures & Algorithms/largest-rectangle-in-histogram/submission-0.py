class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        #edge case        
        if len(heights)==1:
            return heights[0]

        # it is possible that we can only form across one cell
        # maxheight = 0 
        # for height in heights:
        #     if height>maxheight:
        #         maxheight = height
        stack = []
        maxheight = 0
        for ind, height in enumerate(heights):
            # print(stack)
            if not stack or stack and height >= stack[-1][1]:
                stack.append([ind, height])
            else:
                # print(stack)
                while stack and height < stack[-1][1]:
                    indleft, heightleft = stack.pop()
                    # print(indleft)
                    # print(ind)
                    area = (ind - indleft)*heightleft
                    if area > maxheight:
                        maxheight = area
                        print(maxheight)
                stack.append([indleft, height])
        
        print(stack)
        while stack:
            indleft, heightleft = stack.pop()
            area = (ind - indleft+1)*heightleft
            if area > maxheight:
                maxheight = area


        return maxheight