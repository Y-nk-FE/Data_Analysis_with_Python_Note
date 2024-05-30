# Numpy

numpy是python开源的数值计算扩展，这种工具可用来存储和处理大型矩阵


```python
import numpy as np
```

## 产生数组

从列表产生数组


```python
l = [0,1,2,3]
a = np.array(l)
a
```




    array([0, 1, 2, 3])



从列表传入


```python
a = np.array([1,2,3,4,5,6])
a
```




    array([1, 2, 3, 4, 5, 6])



生成全0的数组


```python
np.zeros(2)
```




    array([0., 0.])



生成全1的数组


```python
np.ones(5)
```




    array([1., 1., 1., 1., 1.])




```python
# dtype data_type数据类型
np.ones(5,dtype='bool')
```




    array([ True,  True,  True,  True,  True])



使用fill方法将数组设定为指定的值


```python
a = np.array([1,2,3,4,5])
a.fill(5)
a=a.astype('float')
a
```




    array([5., 5., 5., 5., 5.])



生成整数序列,[a,b)


```python
a = np.arange(0,10)
a
```




    array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])



等差数列

arange(起点，终点，步长)--区间[)

linspace（起点，终点，个数）--区间[]


```python
a = np.arange(0,10,3)        #参数（起点，终点后一位，步长）
a
```




    array([0, 3, 6, 9])




```python
a = np.linspace(0,10,20)     
a
```




    array([ 0.        ,  0.52631579,  1.05263158,  1.57894737,  2.10526316,
            2.63157895,  3.15789474,  3.68421053,  4.21052632,  4.73684211,
            5.26315789,  5.78947368,  6.31578947,  6.84210526,  7.36842105,
            7.89473684,  8.42105263,  8.94736842,  9.47368421, 10.        ])



生成随机数


```python
np.random.rand() # 无参数时默认生成一个随机数
```




    0.6753515249026585




```python
np.random.rand(10) # 括号中参数表述生成的个数
```




    array([0.96140883, 0.70137284, 0.88038565, 0.70551938, 0.52773452,
           0.64095506, 0.60343357, 0.17746041, 0.77166981, 0.91331895])




```python
np.random.randn(10) # randn-服从随机标准正态分布的随机数
```




    array([ 2.05121656, -0.65812416, -0.86593867,  0.45349271, -0.69739058,
           -0.21568942,  1.00760036,  0.8070378 , -0.2507561 ,  0.88493207])




```python
np.random.randint(1,100,10) # 生成随机整数，区间【a，b】，以及生成个数
```




    array([ 9, 92, 35,  5, 79, 71, 70, 84, 92, 95])



## 数组属性 

查看类型


```python
type(a)  # numpy.ndarray - numpy的n维数组，n，dimensionality-维度
```




    numpy.ndarray



数组中的数据的类型


```python
a.dtype
```




    dtype('float64')



查看形状，返回一个一维元组，每个数代表其维度下的数量


```python
a.shape   # 一维数组（20个数据）
```




    (20,)



查看数组的大小


```python
a.size
```




    20



查看数组的维度


```python
a.ndim
```




    1



## 索引和切片

## 多维数组及其属性

参数[lower:upper:step]


```python
a = np.array([[1,2,3,4],[6,7,8,9]])
a
```




    array([[1, 2, 3, 4],
           [6, 7, 8, 9]])




```python
a[0,3]
```




    4




```python
a[1]
```




    array([6, 7, 8, 9])




```python
a[:,1]
```




    array([2, 7])



## 数组的切片 

切片在内存中使用的是引用机制，Python并不会给数组的切片分配新的空间，而是使用引用机制，切片指向来的之前的被切片的数组的地址

## 列表的切片

列表的切片则是分配新的存储空间，和数组的引用不一样，这会造成不必要的存储空间浪费。一个解决方案就是使用Copy()方法来复制，然后便可以达到引用的效果。

## 花式切片

切片只能对于连续或者等间距的数组或者列表进行应用，如果想要对于任意位置进行切片的话，则需呀使用花式切片的方法 fancy slicing

# 一维花式索引


```python
a = np.arange(0,100,10)
a
```




    array([ 0, 10, 20, 30, 40, 50, 60, 70, 80, 90])




```python
index = [1,5,6]
y = a[index]
print(y)
```

    [10 50 60]
    


```python
y
```




    array([10, 50, 60])



或者可以用bool数组进行花式索引


```python
mask = np.array([0,0,0,1,1,0,1,0,1,0],dtype='bool')
y = a[mask]
print(y)
```

    [30 40 60 80]
    

## numpy中的where

where返回索引值


```python
a = np.array([0,2,12,16,20,28,30])
a
```




    array([ 0,  2, 12, 16, 20, 28, 30])




```python
a > 20
```




    array([False, False, False, False, False,  True,  True])




```python
np.where(a>=20)
```




    (array([4, 5, 6], dtype=int64),)



## 数组排序 


```python
a = np.array([0,4,89,45,13,12,2,45,78,56])
a
```




    array([ 0,  4, 89, 45, 13, 12,  2, 45, 78, 56])



sort()排序--对数组进行排序，但是并不会原数组的数据顺序，而是新的临时数组


```python
np.sort(a)
```




    array([ 0,  2,  4, 12, 13, 45, 45, 56, 78, 89])



argsort()排序--按照数值的大小，从小到大返回对应的索引值


```python
np.argsort(a)
```




    array([0, 6, 1, 5, 4, 3, 7, 9, 8, 2], dtype=int64)




```python
for i in np.argsort(a):
    print(a[i])
```

    0
    2
    4
    12
    13
    45
    45
    56
    78
    89
    

## 求和


```python
sum(a)
```




    344




```python
np.sum(a)
```




    344




```python
a.sum()
```




    344



## 最大值


```python
max(a)
```




    89




```python
np.max(a)
```




    89




```python
a.max()
```




    89



## 最小值


```python
min(a)
```




    0




```python
np.min(a)
```




    0




```python
a.min()
```




    0



## 均值


```python
np.mean(a)
```




    34.4




```python
a.mean()
```




    34.4



## 标准差


```python
np.std(a)
```




    31.12940731848263




```python
a.std()
```




    31.12940731848263



## 相关系数矩阵


```python
a = np.array([0,10,25,69,125,280])
b = np.array([0,10,25,69,125,280])
np.cov(a,b)
```




    array([[11266.16666667, 11266.16666667],
           [11266.16666667, 11266.16666667]])



# 多维数组操作

## 数组形状


```python
a = np.arange(6)
a
```




    array([0, 1, 2, 3, 4, 5])



shape - 直接修改原来的数组


```python
a.shape =2,3
a
```




    array([[0, 1, 2],
           [3, 4, 5]])



reshape - 直接生成新的数组


```python
a = np.arange(6)
a.reshape(2,3)
```




    array([[0, 1, 2],
           [3, 4, 5]])




```python
a
```




    array([0, 1, 2, 3, 4, 5])



## 转置


```python
a.reshape(2,3).T
```




    array([[0, 3],
           [1, 4],
           [2, 5]])



## 数组连接

numpy.concatenate（(array1,array2,...),axis = "连接方向定义"）

axis = 0时，按照行连接

axis = 1时，按照列连接


```python
a = np.array([[0,1,2,3,4],[5,6,7,8,9]])
b = np.array([[10,11,12,13,14],[15,16,17,18,19]])
c = np.concatenate((a,b),axis = 0)
c
```




    array([[ 0,  1,  2,  3,  4],
           [ 5,  6,  7,  8,  9],
           [10, 11, 12, 13, 14],
           [15, 16, 17, 18, 19]])




```python
c = np.concatenate((a,b),axis = 1)
c
```




    array([[ 0,  1,  2,  3,  4, 10, 11, 12, 13, 14],
           [ 5,  6,  7,  8,  9, 15, 16, 17, 18, 19]])



## Numpy的内置函数 

vstack


```python
np.vstack((a,b))
```




    array([[ 0,  1,  2,  3,  4],
           [ 5,  6,  7,  8,  9],
           [10, 11, 12, 13, 14],
           [15, 16, 17, 18, 19]])



hstack


```python
np.hstack((a,b))
```




    array([[ 0,  1,  2,  3,  4, 10, 11, 12, 13, 14],
           [ 5,  6,  7,  8,  9, 15, 16, 17, 18, 19]])



dstack


```python
np.dstack((a,b))
```




    array([[[ 0, 10],
            [ 1, 11],
            [ 2, 12],
            [ 3, 13],
            [ 4, 14]],
    
           [[ 5, 15],
            [ 6, 16],
            [ 7, 17],
            [ 8, 18],
            [ 9, 19]]])


