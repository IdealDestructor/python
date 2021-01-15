# ZF2021328 王德强 SVD分解矩阵
from scipy import sparse
import numpy as np
import xlwt
from numpy import linalg as la

col = [0] * 50
row = [0] * 50
data = [0] * 50
# 产生随机位置
for i in range(50):
    row[i] = np.random.randint(0, 50)
    col[i] = np.random.randint(0, 200)
    data[i] = 1
# 构建稀疏矩阵
sparseMatrix = sparse.coo_matrix((data, (row, col)), shape=(50, 200)).toarray()
print(sparseMatrix)
# 创建工作薄保存稀疏矩阵
file = xlwt.Workbook()
sheet = file.add_sheet(u'sheet', cell_overwrite_ok=True)  # 创建sheet
for c in range(200):
    for r in range(50):
        sheet.write(r, c, int(sparseMatrix[r, c]))
file.save('./excel.xls')

# SVD变换：
U, S, V = la.svd(sparseMatrix, full_matrices=0, compute_uv=1)
print(U, U.shape)
print(S, S.shape)
print(V, V.shape)

# 还原初始矩阵
left = np.dot(U, np.diag(S))
result = np.dot(left, V)
print(result, result.shape)
