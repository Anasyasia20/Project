print("Hello,world!!!")

spisok = [3, 8, 5, 9, 1] #Последовательность с размерностью 5
for j in range(1, len(spisok)): #Этот цикл отвечает за количество обходов ( их будет 5)
    for i in range(1, len(spisok)): #Этот код делает один обход по последовательности
        if spisok[i-1] > spisok[i]:
            spisok[i-1], spisok[i] = spisok[i], spisok[i-1]
print(spisok)

