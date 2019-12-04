from math import sqrt
from sklearn import datasets
from sklearn.model_selection import train_test_split
import numpy as np
from sorting_algo.quick_sort import quick_sort


class knn:
    def __init__(self, x_train=0, y_train=0, classes=0, k=0):
        self.x_train = x_train
        self.y_train = y_train
        self.classes = classes
        self.point = None
        self.k = k

    def distances(self):
        summ = 0
        distance = []
        for i in range(len(self.x_train)):
            for j in range(len(self.x_train[0])):
                summ += (self.x_train[i][j] - self.point[j]) ** 2
            distance.append(sqrt(summ))
            summ = 0
        return distance

    def fit(self, x_train, y_train, classes, k=5):
        self.x_train = x_train
        self.y_train = y_train
        self.classes = classes
        self.k = k

    def predict(self, point):
        self.point = point
        dist = self.distances()
        pr = {}
        for i in range(len(self.x_train)):
            pr[dist[i]] = self.y_train[i]
        sort_dist = quick_sort(list(pr.keys()))
        result = []
        for i in sort_dist[:self.k]:
            result.append(pr[i])
        print(result)
        sum = 0
        for i in result:
            sum += i
        return sum/len(result)

def main():
    data = datasets.load_iris()

    X = np.array(data["data"])
    y = np.array(data["target"])
    classes = data["target_names"]

    X_train, X_test, y_train, y_test = train_test_split(X, y)

    model = knn()
    model.fit(X_train, y_train, classes)
    p = model.predict(X_test[3])
    print('predict : ', p)
    print(classes[int(round(p))])
    print(y_test[3])

if __name__ == '__main__':
    main()
# расстояние как оценка модификация