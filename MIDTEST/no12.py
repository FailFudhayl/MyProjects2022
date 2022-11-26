def add(x, y):
    if(x==y):
        return x*2

    bigger, smaller= max(x, y), min(x, y)
    total= (bigger*2) - (bigger-smaller)

    return total

print('Hasil Penjumlahan:',add(*map(int, input('Masukkan x dan y: ').split(' '))))

input_set=[
    [1, 2],
    [-9, 100],
    [4, -4],
    [0, 8]
]