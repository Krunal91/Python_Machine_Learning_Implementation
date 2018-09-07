import numpy as np
from sklearn.datasets import load_breast_cancer


class LogisticRegression():

    def __init__(self):
        pass

    def sigmoid(self, a):
        a = 1 / (1 + np.exp(-a))
        return a

    def train(self, X, y_true, n_iteration, learning_rate):
        n_samples, n_features = X.shape

        self.weights = np.zeros((n_features, 1))
        self.bias = 0
        costs = []

        for i in range(n_iteration):
            a = np.dot(X, self.weights) + self.bias

            y_pred = self.sigmoid(a)

            cost = - (1 / n_samples) * np.sum((y_true * np.log(y_pred)) + ((1 - y_true) * np.log(1 - y_pred)))

            costs.append(cost)

            dw = (1 / n_samples) * np.dot(X.T, (y_pred - y_true))
            db = (1 / n_samples) * np.sum(y_pred - y_true)

            self.weights = self.weights - learning_rate * dw
            self.bias = self.bias - learning_rate * db

            print('Cost after {} iteration : {}'.format(i, cost))

        return self.weights, self.bias

    def predict_prob(self, X):
        y_pred = self.sigmoid(np.dot(X, self.weights) + self.bias)
        return y_pred

    def predict(self, X):
        y_pred = self.predict_prob(X)
        y_pred = [1 if i > 0 else 0 for i in y_pred]
        return y_pred


if __name__ == '__main__':
    X, y = load_breast_cancer(return_X_y=True)
    LG = LogisticRegression()
    LG.train(X, y, n_iteration=10, learning_rate=0.01)
    prob = LG.predict_prob(X)
    label = LG.predict(X)

    print(prob, label)
