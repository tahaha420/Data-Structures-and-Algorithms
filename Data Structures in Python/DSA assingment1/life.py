from array1 import Array2D

class Life_Grid:
    DEAD_CELL = '.'
    LIVE_CELL = '@'

    def __init__(self, numRows, numCols):
        self.rows = numRows
        self.cols = numCols
        self._grid = Array2D(numRows, numCols)
        self.configure(list())

    def numRows(self):
        return self._grid.numRows()

    def numCols(self):
        return self._grid.numCols()

    def __getitem__(self, ndxTuple):
        return self._grid[ndxTuple[0], ndxTuple[1]]

    def configure(self, coordList):
        for i in range(self.rows):
            for j in range(self.cols):
                self.clearCell(i, j)
        for coord in coordList:
            self.setCell(coord[0], coord[1])

    def isLiveCell(self, row, col):
        return self._grid[row, col] == Life_Grid.LIVE_CELL

    def isDead(self, row, col):  # CHECKS FOR THE DEAD CELL
        if self._grid[row, col] == Life_Grid.DEAD_CELL:
            return True
        else:
            return False

    def alive(self, ndxtuple):
        self._grid[ndxtuple[0], ndxtuple[1]] = Life_Grid.LIVE_CELL

    def clearCell(self, row, col):
        self._grid[row, col] = Life_Grid.DEAD_CELL

    def setCell(self, row, col):
        self._grid[row, col] = Life_Grid.LIVE_CELL

    def numLiveNeighbors(self, row, col):
        tmp = 0
        row_above = row - 1 if row > 0 else row
        left_col = col - 1 if col > 0 else col
        right_col = col + \
            1 if col < (self.numCols() - 1) else self.numCols()-1
        row_below = row + \
            1 if row < (self.numRows() - 1) else self.numRows() - 1

        for i in range(row_above, row_below + 1):
            for j in range(left_col, right_col + 1):
                if (i == row and j == col):
                    continue
                if self.isLiveCell(i, j):
                    tmp += 1
        return tmp

    def __iter__(self):
        return self

    def draw(_grid):
        for i in range(_grid.numRows()):
            print('')
            for j in range(_grid.numCols()):
                print(_grid[i, j], end=' ')

        
        
#     def numLiveNeighbors(self, row, col):
#         num = 0
#         for r in [-1, 0, 1]:
#             for c in [-1, 0, 1]:
#                 if r == 0 and c == 0:
#                     continue
#                 if self.isLiveCell(row + r, col + c):
#                     num += 1
        return num
        
    def __iter__(self):
        return self

    def draw(self):
        for i in range(self._grid.numRows()):
            print('')
            for j in range(self._grid.numCols()):
                print(self._grid.__getitem__(i, j), end=' ')
