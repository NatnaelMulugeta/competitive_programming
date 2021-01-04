def triangle2(height):
    for i in range(height + 1):
        print(' '*height , '*'*(2*i-1))
        height -=1

triangle2(15)

