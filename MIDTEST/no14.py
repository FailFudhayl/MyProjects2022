x= int(input('Masukkan tinggi belah ketupat (ganjil) : '))

if x%2==0:
    print('Tinggi belah ketupat tidak ganjil...')
else:
    n = x//2+1
    m = x//2
    for row in range(-m, m+1):
        for col in range(-m, m+1):
            if abs(row) + abs(col) == m:
                c = '*'
            else:
                c = ' '
            print(c, end='')
        print()

input_set= \
[
    [5],
    [6],
    [9],
    [3],
    [1],
    [0],
    [21]
]
