import pandas as pd

def read_excel_column(file_path, sheet_name, column_name, start_row=1, end_row=None):
    """
    从Excel表格中读取指定列的对应行数据
    
    参数:
        file_path (str): Excel文件路径
        sheet_name (str): 工作表名称
        column_name (str/int): 列名(字母)或列索引(从0开始)
        start_row (int): 起始行号(从1开始)
        end_row (int): 结束行号(可选)
    
    返回:
        list: 包含指定列数据的列表
    
    示例:
        data = read_excel_column('data.xlsx', 'Sheet1', 'A', 2, 10)
        data = read_excel_column('data.xlsx', 'Sheet1', 0, 2)  # 读取第1列
    """
    try:
        # 读取Excel文件
        df = pd.read_excel(file_path, sheet_name=sheet_name, header=None)
        
        # 确定行范围
        if end_row is None:
            end_row = len(df)
        
        # 调整行索引(因为pandas从0开始，而输入是从1开始)
        start_idx = start_row - 1
        end_idx = end_row - 1 if end_row else len(df)
        
        # 选择列数据
        if isinstance(column_name, str):
            # 如果是字母列名，转换为列索引
            col_letter = column_name.upper()
            col_idx = ord(col_letter) - ord('A')  # A->0, B->1, etc.
        else:
            col_idx = column_name
        
        # 提取数据并转换为列表
        data = df.iloc[start_idx:end_idx+1, col_idx].tolist()
        
        return data
    
    except FileNotFoundError:
        print(f"错误: 文件 {file_path} 未找到")
        return []
    except Exception as e:
        print(f"读取Excel时发生错误: {str(e)}")
        return []

# 使用示例
if __name__ == "__main__":
    # 示例1: 读取Sheet1中A列第2行到第10行的数据
    data_a = read_excel_column('data.xlsx', 'Sheet1', 'A', 2, 10)
    print("A列数据:", data_a)
    
    # 示例2: 读取第2列(索引1)的所有数据
    data_col2 = read_excel_column('data.xlsx', 'Sheet1', 1, 2)
    print("第2列数据:", data_col2)