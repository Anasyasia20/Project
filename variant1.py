print("Hello,world!!!")

spisok = [3, 8, 5, 9, 1] #Последовательность с длиной 5
for j in range(0, len(spisok)): #цикл отвечает за количество обходов
    for i in range(0, len(spisok)-1): #проход по парам последовательности (кроме последнего элемента, так как он уже макс)
        if spisok[i] > spisok[i+1]:
            spisok[i], spisok[i+1] = spisok[i+1], spisok[i]
print(spisok)
#длина списка = 5. но нумерация чисел начинается с 0, 5 позиции у нас нет, поэтому ставим -1
