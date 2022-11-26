m= int(input('Masukkan panjang kotak: '))
n= int(input('Masukkan lebar kotak: '))

for i in range(n):
    for j in range(m):
        if i==0 or i==n-1:
            print('#', end='')
        elif j==0 or j==m-1:
            print('#', end='')
        else:
            print(end=' ')

    print()

input_set= \
[
    ['4', '4'],
    ['5', '3'],
    ['4', '4'],
    ['5', '3'],
    ['4', '4'],
    ['5', '3'],
    ['1', '3'],
    ['5', '2'],
    ['5', '6'],
    ['6', '3']

]