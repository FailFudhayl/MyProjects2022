arr= list(map(float, input('Masukkan list x: ').split(' ')))

sum_arr= sum(arr)

for idx, i in enumerate(arr):
    print(f'Index: {idx}, Nilai: {i}, Rasio: {(i/sum_arr*100):.2f}%')

input_set=[
    ['5 1.5 3 0.5'],
    ['1 1 1 1 1'],
    ['5 1 3 1'],
    ['9 8 0 1 3 8'],
    ['1']

]