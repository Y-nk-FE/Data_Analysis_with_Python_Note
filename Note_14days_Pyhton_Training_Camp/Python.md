# Python数据分析

## （1）基础知识


```python
num = 3
```

循环语句


```python
for i in range(0,5):
    print(num)
```

    3
    3
    3
    3
    3
    

字符串的加法


```python
str = 'hello'+' world'
str
```




    'hello world'



字符串的索引


```python
str[2]
```




    'l'



字符串的分割


```python
str.split()
```




    ['hello', 'world']



split('x')--x 是分割字符
即遇到x字符就分割


```python
s = 'hello&world'
s.split('&')
```




    ['hello', 'world']



查看字符串长度


```python
len(s)
```




    11



布尔值


```python
a = True
a
```




    True



空值,查看字符串长度为0


```python
a = ''
a
```




    ''




```python
len(a)
```




    0



幂次运算：**


```python
2**4
```




    16



整除运算 // ，向下取整


```python
9//2
```




    4



赋值运算


```python
a = 2
b = 0
b += 1
b *= a
b **= 4 #16
b //=5
b
```




    3



逻辑运算


```python
a = 1
b = 0
a and b
a & b
a or b
a | b
```




    1



## （2）数据结构

列表list，参考C中数组


```python
array = [1,2,3,4,5]
array[2]
```




    3




```python
array = list[1,2,3,4,5]
array
```




    list[1, 2, 3, 4, 5]




```python
list('vhfuipsdhv')
```




    ['v', 'h', 'f', 'u', 'i', 'p', 's', 'd', 'h', 'v']




```python
list('154886134')
```




    ['1', '5', '4', '8', '8', '6', '1', '3', '4']




```python
a = [1,2,3,4]
a.append(5)
a.insert(2,0)
a.pop(0)
a[0:2]
a[::-1]
a
```




    [2, 0, 3, 4, 5]



元组tuple，和list列表功能相似，但是一经初始化后无法修改数据
字典dict{key：value}

```python
mv= {'name':'abc','time':123}
mv.values()
```




    dict_values(['abc', 123])




```python
mv
```




    {'name': 'abc', 'time': 123}




```python
mv['name']
```




    'abc'




```python
mv.keys()
```




    dict_keys(['name', 'time'])



集合set，python用{}来生成集合，集合中不含有相同的元素


```python
s = {1,2,2,2,2,3}
len(s)
```




    3




```python
s1 = s
s
```




    {0, 1, 2, 3, 4}




```python
s1.add(6)
s1
```




    {0, 1, 2, 3, 4, 6}




```python
s1&s

```




    {0, 1, 2, 3, 4, 6}



数据类型转换


```python
a='123.4'
type(a)
```




    str



判断和循环


```python
s = [1,4,5,7]
for i in s:
    print(i)
```

    1
    4
    5
    7
    


```python
for i in range(0,9,2):
    print(i)
```

    0
    2
    4
    6
    8
    


```python

```
