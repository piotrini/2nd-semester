import numpy as np
import math



def RangeQuery(DB, distFunc, Q, eps):
    Point_Neighbors = []
    for point in DB:
        if distFunc(Q, point) <= eps:
            Point_Neighbors.append(point)

    return Point_Neighbors

def distFunc(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)


def DBSCAN_Algorithm(DB, distFunc, eps, minPts):
    Cluster_Counter = 0
    Labels = [0] * len(DB)

    for i in range(len(DB)):
        if Labels[i] != 0:
            continue

        Neighbors = RangeQuery(DB, distFunc, DB[i], eps)


        if len(Neighbors) < minPts:
            Labels[i] = -1  # -1 - szum
            continue

        Cluster_Counter += 1
        Labels[i] = Cluster_Counter
        Seeds = Neighbors

        j = 0
        while j < len(Seeds):
            Point = Seeds[j]

            if Labels[DB.index(Point)] == -1:
                Labels[DB.index(Point)] = Cluster_Counter

            elif Labels[DB.index(Point)] == 0:
                Labels[DB.index(Point)] = Cluster_Counter
                Point_Neighbors = RangeQuery(DB, distFunc, Point, eps)

                if len(Point_Neighbors) >= minPts:
                    Seeds.extend(Point_Neighbors)

            j += 1

    return Labels


DB = [
    [1, 1], [2, 2], [2, 3], [8, 8],
    [8, 9], [25, 80], [24, 81], [23, 79],
    [50, 50], [51, 51], [52, 52]
]


eps = 3
minPts = 2


labels = DBSCAN_Algorithm(DB, distFunc, eps, minPts)

print("Etykiety klastrów:", labels)



