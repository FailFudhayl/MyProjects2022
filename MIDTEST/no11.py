baris_x= int(input('Masukkan banyak baris dari matriks x: '))
kolom_x= int(input('Masukkan banyak kolom dari matriks x: '))

baris_y= int(input('Masukkan banyak baris dari matriks y: '))
kolom_y= int(input('Masukkan banyak kolom dari matriks y: '))

if kolom_x!=baris_y:
    print(f'Jumlah kolom matriks x: {kolom_x} dan baris matriks y: {baris_y} tidak sama, operasi matriks tidak memungkinkan')
else:
    x= [list(map(int, input(f'Masukkan nilai baris ke-{i+1} matriks x ({kolom_x} angka) : ').split(' '))) for i in range(baris_x)]
    y= [list(map(int, input(f'Masukkan nilai baris ke-{i+1} matriks y ({kolom_y} angka) : ').split(' '))) for i in range(baris_y)]
    result = [[0 for __ in range(baris_x)] for _ in range(kolom_y)]

    for i in range(len(x)):
        for j in range(len(y[0])):
            for k in range(len(y)):
                result[i][j] += x[i][k] * y[k][j]

    print('Matriks x:\n'+'\n'.join([' '.join([str(j) for j in i]) for i in x]))
    print('\nMatriks y:\n'+'\n'.join([' '.join([str(j) for j in i]) for i in y]))
    print('\nHasil perkalian matrix x dan y:\n'+'\n'.join([' '.join([str(j) for j in i]) for i in result]))

input_set=[
    [2, 2, 2, 2, '4 5', '2 6', '1 2', '3 4'],
    [2, 2, 2, 2, '1 5', '0 0', '7 -7', '13 24'],
    [2, 3, 3, 2, '1 2 3', '4 0 1', '1 2', '3 1', '-1 2'],
    [3, 3, 3, 3, '1 2 3', '4 -5 -6', '-7 8 9', '3 0 2', '1 1 1', '3 -2 0'],
    [3, 3, 3, 3, '-1 2 13', '-4 -15 0', '-7 1 9', '3 10 -2', '-1 11 -1', '9 -12 0'],
    [1, 3, 2, 1]
]