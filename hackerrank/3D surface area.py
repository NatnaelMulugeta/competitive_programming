
def surfaceArea(A):
    # lets assume matrix M has a*b dimention
    a = len(A)
    b = len(A[0])
    result = a*b*2
    for i in range(a):
        for j in range(b):

            if i == 0:
                result += A[i][j]
            if j == 0:
                result += A[i][j]

            if j != 0:
                result += abs(A[i][j] - A[i][j-1])
            if i != 0:
                result += abs(A[i][j] - A[i-1][j])
                
            if i == a-1:
                result += A[i][j]
            if j == b-1:
                result += A[i][j]

            
    return result


print(surfaceArea([[1, 3, 4], [2, 2, 3], [1, 2, 4]]))

