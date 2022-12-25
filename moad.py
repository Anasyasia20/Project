import numpy as np

###########1 task###########
# Программа находит коэффициенты a, b методом крамера

X = [1, 2, 3, 4, 5]
Y = [2, 4, 6, 8, 10]
n = len(X)

summx, summxy, summy, summx2 = 0, 0, 0, 0
for i in range(0, n):
    summxy += (X[i] * Y[i])
    summx += X[i]
    summy += Y[i]
    summx2 += X[i]*X[i]

a = (n*summxy - summx*summy)/(n*summx2-(summx)*(summx))
b = 1/n * summy - a * (summx/n)
print(a, b)


############2 task линейная регрессия############

#Создадим функцию, которая будет находить обратную матрицу методом гауссовой прогонки

# mini_mas - матрица на входе, от которой хотим найти обратную
# def reverse_matrix(mini_mas):
#     #Создадим расширенную матрицу
#     maxi_mas = np.zeros((len(mini_mas), 2*len(mini_mas)),dtype=float)
#     for i in range(len(mini_mas)):
#         for j in range(2*len(mini_mas)):
#             if j>=len(mini_mas):
#                 if i == j-len(mini_mas):
#                     maxi_mas[i][j]=1
#             else:
#                 maxi_mas[i][j]=mini_mas[i][j]
#     mas = maxi_mas
#
##Преобразование матрицы
##сверху вниз

#     for i in range (0, len(mas)): #заходим в цикл по строкам
#         a = mas[i][i] #сохраняем ii элемент, на него поделим потом
#         for j in range (2*len(mas)): #в цикл по столбцам. их кол-во = 2*кол-во строк
#             mas[i][j] = mas[i][j]/a #чтобы ii элемент стал единичным
#         # print(mas)
#         for k in range (i+1, len(mas)): #переходим на сл строку
#             b = mas[k][i]
#             for j in range(2*len(mas)):
#                 mas[k][j]+=mas[i][j]*(-1)*b #вычитаем предыдущую строку, чтобы занулить (i+1,i) элемент
#         # print(mas) #единицы по главной диагонали и ниже нули
#
##снизу вверх

# for i in range (len(mas)-1,0,-1): #с нижней строки движемся вверх
#         for k in range (i-1, -1, -1): #начинаем с последнего столбца влево
#             b = mas[k][i]
#             for j in range(2*len(mas)):
#                 mas[k][j]-=mas[i][j]*b #
#     # print(mas) #len(mas) = 3
#
# rev_mas = np.zeros((len(mini_mas), len(mini_mas)),dtype=float)
#     for i in range (0,len(mas)):
#         for j in range (0, len(mas)*2):
#             if j>=len(mas):
#                 rev_mas[i][j-len(mas)] = mas[i][j]
#     # print('X^(-1) = ', rev_mas)
#     return(rev_mas)
#
# #Функция находит трансп матрицу

# def transp_matrix(mini_mas):
#     tr_mas = np.zeros((len(mini_mas), len(mini_mas)))
#     for i in range(0, len(mini_mas)):
#         for j in range(0, len(mini_mas)):
#             tr_mas[i][j]=mini_mas[j][i]
#     return(tr_mas)
#
#
# # Алгоритм для линейной регрессии
# Y = np.array([[42000], [144000], [151000]])
# print("Y = ", Y)
# X = np.array([[2310, 2, 20], [2333, 2, 12], [2356, 3, 33]], dtype=float)
# print("X = ", X)
# rm = reverse_matrix(X)
# print('X^(-1) = ', rm)
# tm = transp_matrix(X)
# print("X_tr = ", tm)
# # Разные промежуточные вычисления
# G = np.dot(X, rm) #векторное произведение
# temp = np.dot(tm, X)
# temp_rev = reverse_matrix(temp)
# mf = np.dot(temp_rev, tm)
# B = np.dot(mf, Y)
# print(f"Конечный результат \n B = ", B)

# print(np.dot(X,rm))