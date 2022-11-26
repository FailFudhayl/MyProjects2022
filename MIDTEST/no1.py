p1= int(input('Masukkan n: '))

s= ''
if p1<=0:
    s+= 'A'
elif p1<=100:
    s+= 'B'
elif p1<=200:
    s+= 'C'
else:
    s+= 'D'

s+= str((p1%3)+1)

print(p1,'berada pada kelompok',s)

input_set= \
[
    [10],
    [9],
    [8],
    [-9],
    [234],
    [1900],
    [200],
    [100],
    [0],
]