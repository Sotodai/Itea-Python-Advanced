# 4. Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
f = open('input.txt', encoding='utf-8')
arr = []
for line in f:
    arr.append(line.split())

d = {'One': 'Один', 'Two': 'Два', 'Three':'Три', 'Four':'Четыре'}

g = open('output.txt', 'w', encoding='utf-8')

for i in range(len(arr)):
    for j in range(len(arr[i])):
        t = True
        for l in d.keys():
            if(arr[i][j] == l):
                t = False
                g.write(d[l] + ' ')
        if(t):
            g.write(arr[i][j] + ' ')
    g.write('\n')
