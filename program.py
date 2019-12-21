
# список з 10-ти чисел від 0 до 10
# усі числa які більше 5, збільшіть на 10

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list)
i = []
for i in list:
    if i > 5:
        i += 10
        print(i)
    else:
        print('This number < 5')
