x= int(input('Masukkan x : '))
y= int(input('Masukkan y : '))

res= f'Koordinat : ({x},{y}), berada pada '

if x>=1 and y>=1:
    res+= 'kuadran 1'
elif x<=-1 and y>=1:
    res+= 'kuadran 2'
elif x<=-1 and y<=-1:
    res+= 'kuadran 3'
elif x>=1 and y<=-1:
    res+= 'kuadran 4'
elif x==0 and y==0:
    res+= 'pusat koordinat'
elif x==0:
    res+= 'garis y'
elif y==0:
    res+= 'garis x'

print(res)

input_set= \
[
    [10, -1],
    [9, 9],
    [0, 0],
    [0, 1],
    [1, 0],
    [-1, 1],
    [-2, -2]
]