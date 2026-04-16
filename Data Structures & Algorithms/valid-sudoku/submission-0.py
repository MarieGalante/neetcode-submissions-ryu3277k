from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #rules that I need to satisfy
        # check row for duplicates
        # check column for duplicates

        # for col in range(9):
        #     # check that all rows don't have duplicates

        # check the rows
        for row in range(9):
            currow = board[row]
            checkdup = defaultdict(int)

            # col = 1
            # checkdup[currow[col]]
            for col in range(9):
                if currow[col].isalnum():
                    if checkdup[currow[col]]==0:
                        checkdup[currow[col]] += 1
                    else:
                        return False
        

        # check the columns for validity
        for col in range(9):
            
            checkdup = defaultdict(int)
            for row in range(9):
                if board[row][col].isalnum():
                    if checkdup[board[row][col]] == 0:
                        checkdup[board[row][col]] += 1
                    else:
                        return False
            # curcol = board[:][col]
            # print(curcol)

        # now loop through the inner blocks
        for i in range(3):

            for j in range(3):
                checkdup = defaultdict(int)
                
                # loop through the interior of each loop
                for ii in range(3):

                    for ij in range(3):
                        curnum = board[ (i-1)*3 + ii][ (j-1)*3 +ij]
                        if curnum.isalnum():
                            if checkdup[curnum] == 0:
                                checkdup[curnum] += 1
                            else:
                                return False



        return True
            

                