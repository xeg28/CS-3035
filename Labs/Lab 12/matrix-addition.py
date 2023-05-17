def matrixAdd(A, B, SUM):
    for i in range(3): #iterates through the rows
        for j in range(3): #iterates through the columns
            SUM[i].append(A[i][j] + B[i][j]) #adds and appends the result
    return SUM #returns the resul
    
def matrixAddAsString(A, B, SUM):
    for i in range(3): #iterates through the rows
        for j in range(3): #iterates through the columns
            SUM[i].append(str(A[i][j]) + str(B[i][j])) #casts the values to string then concatinates them and appends to the result
    return SUM #returns the result  
    
def printMatrix(m): #prints the matrix
    for i in range(3):
        for j in range(3):
            print(m[i][j], end=" ")
        print()
              
A = [[1,2,3],[4,5,6],[7,8,9]] #matrix1
B = [[9,8,7],[6,5,4],[3,2,1]] #matrix2
SUM = [[],[],[]] #empty matrix

SUM = matrixAdd(A,B,SUM)
printMatrix(SUM)
print()
SUM = [[],[],[]]#empty matrix
SUM = matrixAddAsString(A,B,SUM)
printMatrix(SUM)
