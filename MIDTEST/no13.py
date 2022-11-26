def compareTriplets(a, b):
    a_score, b_score= 0, 0
    
    for i in range(3):
        if(a[i]>b[i]):
            a_score+= 1
        elif(a[i]<b[i]):
            b_score+= 1
            
    return a_score, b_score

a= list(map(int, input('Masukkan triplet a: ').split(' ')))
b= list(map(int, input('Masukkan triplet b: ').split(' ')))

if len(a)!=3:
    print('Panjang a tidak sama dengan 3')
elif len(b)!=3:
    print('Panjang b tidak sama dengan 3')
else:
    print(f'Skor triplet a: {compareTriplets(a,b)[0]}')
    print(f'Skor triplet b: {compareTriplets(a,b)[1]}')

input_set= \
[
    ['1 2 3', '4 5 6'],
    ['12 39 87', '12 39 0'],
    ['1', '1'],
    ['1 2 900', '2 1 98']
]
