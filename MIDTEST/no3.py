def compute_lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y

    while (True):
        if ((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1

    return lcm


num1 = int(input('Masukkan x: '))
num2 = int(input('Masukkan y: '))

print(f"KPK dari {num1} dan {num2}:", compute_lcm(num1, num2))

input_set = [
    [4, 6],
    [4, 2],
    [3, 7],
    [5, 5],
    [1, 10],
    [32, 33],
    [123, 2]
]
