def gcd(n1,n2):
    if(n1==0):
        return n2
    else:
        return gcd(n2%n1,n1)

n1=int(input('Masukkan angka pertama: '))
n2=int(input('Masukkan angka kedua: '))
n3=int(input('Masukkan angka ketiga: '))

print(f'FPB dari {n1}, {n2} dan {n3}: {gcd(n1,gcd(n2,n3))}')

input_set=[
    [2, 4, 6],
    [8, 6, 3],
    [1, 3, 7],
    [9, 9, 8],
    [8, 8, 8]
]
