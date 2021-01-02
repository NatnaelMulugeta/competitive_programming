def triangle2(height):
    depth = height // 2
    for i in range(height + 1):
        if i % 2 == 1:
            print(' '*depth , '*'*i)
            depth -=1

triangle2(16)

