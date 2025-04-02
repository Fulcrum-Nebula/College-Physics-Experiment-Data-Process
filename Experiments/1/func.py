import numpy as np
from scipy.optimize import curve_fit

class ExponentialFit:
    def __init__(self, x_data, y_data):
        """
        初始化指数拟合类
        :param x_data: x 值列表
        :param y_data: y 值列表
        """
        self.x_data = np.array(x_data)
        self.y_data = np.array(y_data)
        self.params = None
        self.covariance = None
        
    @staticmethod
    def _exponential_func(x, a, b, c):
        """定义拟合函数: a + b * e^(c * x)"""
        return a + b * np.exp(c * x)
    
    def fit(self, initial_guess=(1, 1, -1)):
        """
        执行拟合
        :param initial_guess: 初始猜测参数 (a, b, c)
        :return: 拟合参数 (a, b, c)
        """
        self.params, self.covariance = curve_fit(
            self._exponential_func, 
            self.x_data, 
            self.y_data, 
            p0=initial_guess,
            maxfev=10000  # 增加最大迭代次数
        )
        return self.params
    
    def get_equation(self):
        """返回拟合方程的字符串表示"""
        if self.params is None:
            raise ValueError("请先调用 fit() 方法进行拟合")
        a, b, c = self.params
        return f"y = {a:.4f} + {b:.4f} * e^({c:.4f} * x)"
    
    def predict(self, x):
        """使用拟合方程预测新的 y 值"""
        if self.params is None:
            raise ValueError("请先调用 fit() 方法进行拟合")
        return self._exponential_func(x, *self.params)
    
    def get_r_squared(self):
        """计算并返回 R² 值"""
        if self.params is None:
            raise ValueError("请先调用 fit() 方法进行拟合")
        residuals = self.y_data - self.predict(self.x_data)
        ss_res = np.sum(residuals**2)
        ss_tot = np.sum((self.y_data - np.mean(self.y_data))**2)
        r_squared = 1 - (ss_res / ss_tot)
        return r_squared