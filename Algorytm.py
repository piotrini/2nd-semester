import math
import random

import matplotlib.pyplot as plt
import numpy as np

# Funkcja sprawdzająca czy odległość pomiędzy punktem orientacyjnym Q, a między punktem z zestawu danych jest mniejsza lub równa podanemu epsilon.

def RangeQuery(DB, distFunc, Q, eps):
    Point_Neighbors = []
    for point in DB:
        if distFunc(Q, point) <= eps:
            Point_Neighbors.append(point)

    return Point_Neighbors

# Funkcja obliczająca odległość pomiędzy dwoma punktami.

def distFunc(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Algorytm klastrujący podane punkty.

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

# Rysowanie wykresu z klastrami

def plot_clusters(DB, labels):
    # Pobieramy unikalne etykiety klastrów (w tym szum -1)
    unique_labels = set(labels)

    # Przypisujemy różne kolory do klastrów
    colors = plt.cm.rainbow(np.linspace(0, 1, len(unique_labels)))

    for label, color in zip(unique_labels, colors):
        # Wybieramy punkty należące do danego klastra
        cluster_points = [DB[i] for i in range(len(DB)) if labels[i] == label]

        # Szum (punkty oznaczone jako -1) będzie czarny
        if label == -1:
            color = 'black'
            cluster_label = "Szum"
        else:
            cluster_label = f"Klaster numer {label}"

        cluster_points = np.array(cluster_points)

        # Rysowanie punktów na wykresie
        plt.scatter(cluster_points[:, 0], cluster_points[:, 1], c=[color], label=cluster_label)

    # Ustawienia wykresu
    plt.title("Wynik klasteryzacji DBSCAN")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend(loc='upper left', bbox_to_anchor=(1.05, 1), title="Legenda")
    plt.grid(True)
    plt.show()



DB = [
    # Klaster 0
    [1, 1], [3, 3], [2, 5], [4, 2], [1, 6], [5, 5], [3, 1], [2, 3], [1, 4],
    [4, 4], [3.5, 2.5], [1.2, 5.8], [2.7, 1.1], [4.6, 3.2], [3.1, 4.5],
    [5, 2], [1.8, 6.2], [2.9, 5.7], [4.3, 3.9], [5.4, 1.3],

    # Klaster 1
    [8, 8], [10, 9], [9, 11], [11, 8], [10, 10], [7, 12], [12, 9], [8, 10],
    [9.5, 8.7], [11.3, 10.1], [10.7, 8.9], [9.2, 11.8], [8.6, 9.3], [11, 11],
    [7.8, 11.5], [12.1, 10.8], [10.9, 12.2], [8.7, 10.3], [9.4, 9.9],

    # Klaster 2
    [14, 14], [16, 15], [15, 17], [17, 14], [16, 16], [13, 18], [18, 15],
    [14, 16], [15.5, 14.7], [17.3, 16.1], [16.8, 14.9], [15.2, 17.8],
    [14.6, 15.3], [17, 17], [13.8, 17.5], [18.1, 16.8], [16.9, 18.2],
    [14.7, 16.3], [15.4, 15.9],

    # Klaster 3
    [18, 18], [20, 19], [19, 20], [20, 18], [19, 19], [17, 20], [20, 17],
    [18, 20], [19.5, 18.7], [20.3, 19.1], [19.7, 18.9], [18.2, 20.8],
    [18.6, 19.3], [20, 20], [17.8, 19.5], [20.1, 20.8], [19.9, 20.2],
    [18.7, 19.3], [19.4, 19.9],

    # Punkty szumu
    [3, 17], [12, 5], [7, 15], [6, 12], [19, 4]
]




# for x in range(1,100):
#     DB.append([random.uniform(1.00, 100.00), random.uniform(1.00,100.00)])

print(DB)


eps = 2
minPts = 2


labels = DBSCAN_Algorithm(DB, distFunc, eps, minPts)

print("Etykiety klastrów:", labels)

plot_clusters(DB, labels)



