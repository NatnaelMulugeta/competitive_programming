def kClosest(points, k):
    dis = []
    for i in points:
        d = i[0]**2 + i[1]**2
        dis.append(d)

    dis, points = zip(*sorted(zip(dis, points)))
    return list(points[:k])

print(kClosest([[1,3],[-2,2]], 1))
print(kClosest([[3,3],[5,-1],[-2,4]], 2))

