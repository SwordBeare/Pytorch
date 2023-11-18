import numpy as np
#np是一个对象
arr1 = np.array([1,2,3,4,5])#一维
arr2 = np.array([[1,2,3],[4,5,6]])#二维
arr3 = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])#三维

print(arr1.ndim)#输出维度
arr5 = np.array([1,2,3,4,5],ndmin = 5)#一维设置为五维数组

#访问第二维数据
arr2[0,-1]

#裁切
print(arr1[1::1])
print(arr2[1, 1:3])
print(arr2[0:, 1:3])#总裁剪操作



