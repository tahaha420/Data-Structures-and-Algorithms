from array1 import Array2D

class Life_Grid:
    DEAD_CELL = '.'
    LIVE_CELL = '@'

    def __init__(self, numRows, numCols):
        # self.num_rows = numRows
        # self.num_cols = numCols
        self.grid = Array2D(numRows, numCols)
        self.configure(list())

    def numRows(self):
        return self.grid.numRows()

    def numCols(self):
        return self.grid.numCols()

    def __getitem__(self, ndxTuple):
        return self.grid[ndxTuple[0], ndxTuple[1]]

    def configure(self, coordList):
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                self.clearCell(i, j)
        for coord in coordList:
            self.setCell(coord[0], coord[1])

    def isLiveCell(self, row, col):
        return self.grid[row, col] == Life_Grid.LIVE_CELL

    def alive(self, ndxtuple):
        self.grid[ndxtuple[0], ndxtuple[1]] = Life_Grid.LIVE_CELL

    def clearCell(self, row, col):
        self.grid[row, col] = Life_Grid.DEAD_CELL

    def setCell(self, row, col):
        self.grid[row, col] = Life_Grid.LIVE_CELL

    def numLiveNeighbors(self, row, col):
        num = 0
        for r in [-1, 0, 1]:
            for c in [-1, 0, 1]:
                if r == 0 and c == 0:
                    continue
                if self.isLiveCell(row + r, col + c):
                    num += 1
        return num

    def __iter__(self):
        return self

    def draw(grid):
        for i in range(grid.numRows()):
            print('')
            for j in range(grid.numCols()):
                print(grid[i, j], end=' ')

a = Life_Grid(5, 5)
a.numLiveNeighbors(5,5)
a.alive((1, 2))
a.alive((1, 3))
a.alive((1, 1))
a.alive((2, 0))
a.alive((2, 4))
a.alive((3, 1))
a.alive((3, 3))
a.alive((4, 2))
a.draw()
