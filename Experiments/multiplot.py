import numpy as np
import matplotlib.pyplot as plt

class MultiExponentialPlotter:
    def __init__(self, figsize=(10, 6)):
        """
        初始化多曲线绘图类
        :param figsize: 图形大小
        """
        self.fig, self.ax = plt.subplots(figsize=figsize)
        self.ax.set_xlabel('U(V)')
        self.ax.set_ylabel('I(mA)')
        self.ax.grid(True)
        
    @staticmethod
    def exponential_func(x, a, b, c):
        """指数函数定义: a + b * e^(c * x)"""
        return a + b * np.exp(c * x)
    
    def add_dataset(self, x_data, y_data, params=None, 
                   point_style='o', line_style='-', 
                   label='Data', color=None):
        """
        添加一组数据和拟合曲线到图中
        :param x_data: x值列表
        :param y_data: y值列表
        :param params: 拟合参数 (a, b, c)，如果为None则只绘制数据点
        :param point_style: 数据点样式
        :param line_style: 曲线样式
        :param label: 图例标签
        :param color: 统一颜色（可选）
        """
        x_data = np.array(x_data)
        y_data = np.array(y_data)
        
        # 绘制数据点
        self.ax.plot(x_data, y_data, 
                    marker=point_style if point_style else None,
                    linestyle='',  # 不要连接线
                    label=label if params is None else f'{label} (Data)',
                    color=color)
        
        # 如果提供了参数，绘制拟合曲线
        if params is not None:
            a, b, c = params
            x_min, x_max = min(x_data), max(x_data)
            x_smooth = np.linspace(x_min, x_max, 100)
            y_smooth = self.exponential_func(x_smooth, a, b, c)
            
            self.ax.plot(x_smooth, y_smooth, 
                        linestyle=line_style,
                        label=f'{label} (Fit): y = {a:.3f} + {b:.3f}*e^({c:.3f}*x)',
                        color=color if color else None)

        # 创建次坐标轴（共享 x 轴，右侧 y 轴）
        self.ax2 = self.ax.twinx()  # twinx() 表示共享 x 轴

        x_min, x_max = min(x_data), max(x_data)
        x_smooth = np.linspace(x_min, x_max, 100)
        y_smooth = x_smooth * self.exponential_func(x_smooth, a, b, c)

        # 绘制第二个函数（右侧 y 轴）
        self.ax2.plot(x_smooth, y_smooth, linestyle=line_style, label='P = UI', color=color)
        self.ax2.set_ylabel('P(mW)', color='black')
        self.ax2.tick_params(axis='y', labelcolor='black')

        # 合并图例（需手动合并）
        lines1, labels1 = self.ax.get_legend_handles_labels()
        lines2, labels2 = self.ax2.get_legend_handles_labels()
        self.ax.legend(lines1 + lines2, labels1 + labels2, loc='upper left')
    
    def show(self, title='Multiple Exponential Fits'):
        """显示图形"""
        self.ax.set_title(title)
        self.ax.legend()
        plt.tight_layout()
        plt.show()
        
    def save(self, filename='multi_exponential_fit.png', dpi=300):
        """保存图形"""
        self.fig.savefig(filename, dpi=dpi)
        print(f"图形已保存为 {filename}")