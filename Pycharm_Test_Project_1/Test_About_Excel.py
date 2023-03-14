# 导入pandas库
import pandas as pd
# 导入numpy库
import numpy as np

# Excel文件路径,r对路径进行转义，windows系统的需要
Excel_file_path = r'D:\sample\Data_Analysis_with_Python_Note\Pycharm_Test_Project_1\Date\test_for_anatsql1_fundTable.xlsx'
row_date = pd.read_excel(Excel_file_path,0)
print(row_date)
print('-------------------------------------------------------------------------------------------------')

# values-仅提取表中的数据，提取出来的数据储存到数组中
date = row_date.values
print(date)
print('-------------------------------------------------------------------------------------------------')

# 提取表中的特定数据,注意：存取在数组中的数据的索引值index是从0开始的
# 提取第一行数据
row_1_date = date[0]
print(row_1_date)
print('-------------------------------------------------------------------------------------------------')

# 提取第一列数据，冒号‘:’表示所有行，即All ROWS
column_1_date = date[:, 0]
print(column_1_date)
print('-------------------------------------------------------------------------------------------------')

# 提取第一行，第二列
row_1_column_1_date = date[0, 1]
print(row_1_column_1_date)
print('-------------------------------------------------------------------------------------------------')

# TODO
# 对两部分特征进行拼接组合,np.hstack（）函数和 np.vstack（）函数
# 这里是np.vstack()函数。主要是进行竖直堆叠，使用这个函数的时候要保证两个数组列数是一致的（都是三列），得出的结果如下。
# 下面是np.hstack()函数，主要是进行水平堆叠，使用这个函数的时候要保证行数是一致的（都是两行）。
feature_1 = date[:, 0]    # 取前两列
feature_2 = date[:, 2]    # 取四五列
print(feature_1)
print(feature_2)
#feature_choose =np.stack(feature_1,feature_2)
#print(feature_choose)

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
#print(np.vstack(arr1, arr2))
