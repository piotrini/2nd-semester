import numpy as np




def RangeQuery(DB, distFunc, Q, eps):
    Point_Neighbors = []
    for point in DB:
        if distFunc(Q, point) <= eps:
            Point_Neighbors.append(point)

    return Point_Neighbors

def DBSCAN_Algorithm(DB, distFunc, eps, minPts):
    Cluster_Counter = 0


DB = np.random.rand(20, 2) * 10
print(DB)



