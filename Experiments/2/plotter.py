import numpy as np
import matplotlib.pyplot as plt

class plotter:
    def __init__(self):
        self.fig, self.ax = plt.subplots()  # 初始化画布和坐标轴
        self.datasets = []  # 存储数据集和可选函数
    
    def add_dataset(self, x_data, y_data, marker_style, label, color, func=None, line_style='-'):
        """添加数据集，并可选叠加函数曲线
        
        参数:
            x_data (array-like): x 轴数据
            y_data (array-like): y 轴数据
            marker_style (str): 数据点样式（如 'o', 's'）
            label (str): 数据标签（用于图例）
            color (str): 数据点颜色
            func (callable, optional): 要绘制的函数（如 lambda x: k*x）
            line_style (str): 函数线型（如 '-', '--'）
        """
        self.datasets.append({
            'x_data': np.asarray(x_data),
            'y_data': np.asarray(y_data),
            'marker_style': marker_style,
            'label': label,
            'color': color,
            'func': func,
            'line_style': line_style
        })
    
    def show(self, title=None, xlabel=None, ylabel=None, grid=True):
        """显示图表
        
        参数:
            title (str, optional): 图表标题
            xlabel (str, optional): x 轴标签
            ylabel (str, optional): y 轴标签
            grid (bool, optional): 是否显示网格（默认 True）
        """
        for dataset in self.datasets:
            # 绘制数据点
            self.ax.plot(
                dataset['x_data'], 
                dataset['y_data'], 
                dataset['marker_style'], 
                label=dataset['label'], 
                color=dataset['color']
            )
            
            # 如果传入了函数，绘制曲线
            if dataset['func'] is not None:
                x_min, x_max = np.min(dataset['x_data']), np.max(dataset['x_data'])
                x_func = np.linspace(x_min, x_max, 100)
                y_func = dataset['func'](x_func)
                
                self.ax.plot(
                    x_func, 
                    y_func, 
                    dataset['line_style'], 
                    label=f"{dataset['label']} (Fit)", 
                    color=dataset['color'],
                    alpha=0.7
                )
        
        # 设置标题和坐标轴标签
        if title:
            self.ax.set_title(title)
        if xlabel:
            self.ax.set_xlabel(xlabel)  # 设置x轴标签
        if ylabel:
            self.ax.set_ylabel(ylabel)  # 设置y轴标签
        
        self.ax.legend()
        if grid:
            self.ax.grid(True)
        
        plt.show()