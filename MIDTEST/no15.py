def hurdleRace(k, height):
    max_height= max(height)
    
    if(k>max_height):
        return 0
    else:
        return max_height-k

k= int(input('Masukkan panjang awal lompatan k: '))
arr= list(map(float, input('Masukkan rintangan r: ').split(' ')))

print(f'Ramuan lompat yang dibutuhkan: {int(hurdleRace(k, arr))}')

input_set= \
[
    ['4', '1 6 3 5 2'],
    ['7', '2 5 4 5 2'],
    ['3', '1 3 4 2 3 3 0'],
    ['1', '0 2 1 3 1'],
    ['5', '1 2 3 4'],
    ['1', '4 5 6 1 2 6'],
    ['2', '0 0 0'],
    ['3', '1 3 5 2 3'],
]