text_file = open("number.txt", "r")
lines = text_file.readlines()
for line in lines:
    kaput = line.split()
for j in range(0, len(kaput)):
    for i in range(0, len(kaput)-1):
        if kaput[i] > kaput[i+1]:
            kaput[i], kaput[i+1] = kaput[i+1], kaput[i]
print(kaput)
