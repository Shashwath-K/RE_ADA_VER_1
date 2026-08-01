import numpy as np


class LinearRegression:
    def __init__(self):
        self.coef_ = None
        self.intercept_ = None

    def fit(self, X, y):
        X = np.array(X)
        y = np.array(y)

        if X.ndim == 1:
            X = X.reshape(-1, 1)

        X_b = np.column_stack([np.ones(X.shape[0]), X])

        theta = np.linalg.inv(X_b.T @ X_b) @ X_b.T @ y

        self.intercept_ = theta[0]
        self.coef_ = theta[1:]

    def predict(self, X):
        X = np.array(X)
        if X.ndim == 1:
            X = X.reshape(-1, 1)
        return X @ self.coef_ + self.intercept_

    def r2_score(self, y_true, y_pred):
        y_true = np.array(y_true)
        y_pred = np.array(y_pred)
        ss_res = np.sum((y_true - y_pred) ** 2)
        ss_tot = np.sum((y_true - np.mean(y_true)) ** 2)
        return 1 - (ss_res / ss_tot)


if __name__ == "__main__":
    heights = np.array([150, 160, 170, 180, 190])
    weights = np.array([50, 60, 68, 75, 85])

    model = LinearRegression()
    model.fit(heights, weights)

    print(f"Intercept: {model.intercept_}")
    print(f"Coefficient: {model.coef_}")

    predictions = model.predict(heights)
    print(f"Predictions: {predictions}")
    print(f"R² Score: {model.r2_score(weights, predictions)}")
