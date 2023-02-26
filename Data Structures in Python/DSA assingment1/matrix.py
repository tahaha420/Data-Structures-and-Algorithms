from array1 import Array2D

class Matrix:
    def __init__(self, numRows, numCols):
        self._theGrid = Array2D(numRows, numCols)
        self._theGrid.clear(0)

    def numRows(self):
        return self._theGrid.numRows()

    def numCols(self):
        return self._theGrid.numCols()

    def __getitem__(self, ndxTuple):
        return self._theGrid[ndxTuple[0], ndxTuple[1]]

    def __setitem__(self, ndxTuple, Scalar):
        self._theGrid[ndxTuple[0], ndxTuple[1]] = Scalar

    def scaleBy(self, Scalar):
        for r in range(self.numRows()):
            for c in range(self.numCols()):
                self[r, c] *= Scalar

    def __add__(self, rhsMatrix):
        assert rhsMatrix.numRows() == self.numRows() and \
            rhsMatrix.numCols() == self.numCols(), \
            "Matrix size not compitable with addition operation."

        newMatrix = Matrix(self.numRows(), self.numCols())

        for r in range(self.numRows()):
            for c in range(self.numCols()):
                newMatrix[r, c] = self[r, c] + rhsMatrix[r, c]

        return newMatrix

    def __sub__(self, rhsMatrix):
        assert rhsMatrix.numRows() == self.numRows() and \
            rhsMatrix.numCols() == self.numCols(), \
            "Matrix size not compitable with addition operation."
        newMatrix = Matrix(self.numRows(), self.numCols())
        for r in range(self.numRows()):
            for c in range(self.numCols()):
                newMatrix[r, c] = self[r, c] - rhsMatrix[r, c]
        return newMatrix

    def __mul__(self, rhsMatrix):
        assert rhsMatrix.numCols() == self.numRows(), \
            "Matrix size not compitable with multiplacation operation."
        newMatrix = Matrix(self.numRows(), self.numCols())
        for r in range(self.numRows()):
            for c in range(rhsMatrix.numCols()):
                for cx in range(self.numCols()):
                    newMatrix[r, c] += self[r, cx] * rhsMatrix[cx, c]

        return newMatrix

    
    def transpose(self):
        assert self.numCols() == self.numRows(), \
            "Matrix size not compitable with transpose operation."
        newMatrix = Matrix(self.numRows(), self.numCols())
        for r in range(self.numRows()):
            for cx in range(self.numCols()):
                    newMatrix[r, cx] = self[cx, r] 
    
        return newMatrix
    
    def determinant(self):
        assert self.numCols() == self.numRows(), \
            "Matrix size not compitable with determinant operation."
        newMatrix = Matrix(self.numRows(), self.numCols())
        
        return (self.__getitem__((0,0))*self.__getitem__((1,1)))-(self.__getitem__((0,1))*self.__getitem__((1,0)))
    
    def inverse(self):
        if self.determinant()!=0:
            
            newMatrix = Matrix(self.numRows(), self.numCols())

            temp=self.__getitem__((0,0))
            newMatrix.__setitem__((0,0),self.__getitem__((1,1)))
            newMatrix.__setitem__((1,1),temp)
            newMatrix.__setitem__((1,0),-self.__getitem__((1,0)))
            newMatrix.__setitem__((0,1),-self.__getitem__((0,1)))

            newMatrix.scaleBy(1/(-1*newMatrix.determinant()))
            return newMatrix
        else:
            print("No inverse since determinant is 0")
         
        
        

         
            
            
            
        
def display(x):
    for i in range(x.numRows()):
        print('')
        for j in range(x.numCols()):
            print(x[i, j], end=' ')

def setitem(x):
    for i in range(x.numRows()):
        print('')
        for j in range(x.numCols()):
            x[i, j] = int(input('Enter value %d, %d=' % (i, j)))


