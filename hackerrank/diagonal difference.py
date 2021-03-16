
def diagonalDifference(arr):
    # Write your code here
    result = 0
    d1, d2 = 0, 0
    
    for i in range(len(arr)):
        d1 += arr[i][i]
        d2 += arr[i][len(arr) - 1 - i]
        
    result = abs(d1 - d2)
    
    return result