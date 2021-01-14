def allCellsDistOrder(r, c, r0, c0):
    mat, dis = [], []
    for i in range(r):
        for j in range(c):
            mat.append([i,j])
            dis.append(abs(r0-i) + abs(c0-j))

    dis, mat = zip(*sorted(zip(dis, mat)))
    return mat

print(allCellsDistOrder(2,3,1,2))