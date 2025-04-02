import numpy as np

def linear_regression_through_origin(x, y):
    """
    计算满足 y = kx 的线性回归斜率 k（无截距项）
    
    参数:
        x (array-like): 自变量数据
        y (array-like): 因变量数据
    
    返回:
        float: 斜率 k
    """
    x = np.asarray(x)
    y = np.asarray(y)
    
    if len(x) != len(y):
        raise ValueError("x 和 y 的长度必须相同")
    
    k = np.sum(x * y) / np.sum(x ** 2)
    return k