import numpy as np
import matplotlib.pyplot as plt

class ExponentialFunctionPlotter:
    def __init__(self, x_data, y_data, params=None):
        """
        初始化绘图类
        :param x_data: x 值列表
        :param y_data: y 值列表
        :param params: 可选，三元组参数 (a, b, c)
        """
        self.x_data = np.array(x_data)
        self.y_data = np.array(y_data)
        self.params = params
        self.fig, self.ax = plt.subplots(figsize=(10, 6))
        
    @staticmethod
    def exponential_func(x, a, b, c):
        """指数函数定义: a + b * e^(c * x)"""
        return a + b * np.exp(c * x)
    
    def plot_data(self, point_style='bo', label='Data'):
        """绘制原始数据点"""
        self.ax.plot(self.x_data, self.y_data, point_style, label=label)
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.grid(True)
        
    def plot_function(self, params=None, line_style='b-', label='Fit', num_points=100):
        """
        绘制指数函数曲线
        :param params: 三元组 (a, b, c)，如果为None则使用self.params
        :param line_style: 线条样式
        :param label: 图例标签
        :param num_points: 生成曲线的点数
        """
        if params is None:
            params = self.params
        if params is None:
            raise ValueError("未提供函数参数")
            
        a, b, c = params
        # 生成平滑曲线的x值
        x_min, x_max = min(self.x_data), max(self.x_data)
        x_smooth = np.linspace(x_min, x_max, num_points)
        y_smooth = self.exponential_func(x_smooth, a, b, c)
        
        self.ax.plot(x_smooth, y_smooth, line_style, label=f'{label}: y = {a:.3f} + {b:.3f}*e^({c:.3f}*x)')
        
    def show(self, title='Exponential Function Fit'):
        """显示图形"""
        self.ax.set_title(title)
        self.ax.legend()
        plt.tight_layout()
        plt.show()
        
    def save(self, filename='exponential_fit.png', dpi=300):
        """保存图形"""
        self.fig.savefig(filename, dpi=dpi)
        print(f"图形已保存为 {filename}")


# 使用示例
if __name__ == "__main__":
    # 示例数据
    x = [0, 1, 2, 3, 4, 5]
    y = [2.1, 1.5, 1.1, 0.8, 0.6, 0.5]
    
    # 示例参数 (a, b, c)
    params = (2.0, -1.0, -0.5)
    
    # 创建绘图对象
    plotter = ExponentialFunctionPlotter(x, y, params)
    
    # 绘制数据点
    plotter.plot_data(point_style='bo', label='Original Data')
    
    # 绘制拟合曲线
    plotter.plot_function(params=params, line_style='r--', label='Exponential Fit')
    
    # 显示图形
    plotter.show(title='Exponential Function Demonstration')
    
    # 保存图形（可选）
    # plotter.save('my_fit.png')