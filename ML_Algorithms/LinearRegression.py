import numpy as np
from sklearn.datasets import load_diabetes


class LinearRegression():

    def __init__(self):
        pass

    def train(self, X, y, n_iteration, learning_rate):
        n_samples, n_features = X.shape
        self.weights = np.zeros((n_features, 1))
        self.bias = 0

        costs = []

        for i in range(n_iteration):
            y_pred = np.dot(X, self.weights) + self.bias
            mse = 1 / (n_samples) * np.sum(np.square((y_pred - y)))
            costs.append(mse)

            dw = (2 / n_samples) * np.dot(X.T, (y_pred - y))
            db = (2 / n_samples) * np.sum(y_pred - y)

            self.weights = self.weights - learning_rate * dw
            self.bias = self.bias - learning_rate * db

            print("MSE for iteration {} is : {}".format(i, mse))
        return

    def predict(self, X):
        y_pred = np.dot(X, self.weights) + self.bias
        return y_pred


if __name__ == '__main__':
    X, y = load_diabetes(return_X_y=True)
    LR = LinearRegression()
    LR.train(X, y, 100, 0.001)
    y_pred = LR.predict(X)
