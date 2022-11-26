def miniMaxSum(arr):
    sum_list= []
    for i in arr:
        temp_arr= arr.copy()
        temp_arr.remove(i)
        sum_list.append(sum(temp_arr))
    
    return min(sum_list), max(sum_list)

arr= list(map(int, input('Masukkan list dengan panjang 5: ').split(' ')))

if len(arr)!=5:
    print('Panjang list tidak sama dengan 5')
else:
    print(f'Penjumlahan minimum: {miniMaxSum(arr)[0]}')
    print(f'Penjumlahan maksimal: {miniMaxSum(arr)[1]}')

input_set= \
[
    ['1 2 3 4 5'],
    ['-900 1 2 3 900'],
    ['1 1'],
    ['1 1 1 1 98']
]
