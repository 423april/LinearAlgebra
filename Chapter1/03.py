"""
다음과 같은 행렬과 벡터들의 크기를 출력하는 프로그램을 작성하라
"""

import numpy as np


A = np.array([[1,2,3],[4,5,6],[7,8,9]])
v = np.array([[1],[2],[3]])
w = np.array([[1,2,3]])
B = np.array([[1,2,3],[4,5,6]])

print("A has size {}x{}".format(np.shape(A)[0], np.shape(A)[1]))
print("v has size {}x{}".format(np.shape(v)[0], np.shape(v)[1]))
print("w has size {}x{}".format(np.shape(w)[0], np.shape(w)[1]))
print("B has size {}x{}".format(np.shape(B)[0], np.shape(B)[1]))