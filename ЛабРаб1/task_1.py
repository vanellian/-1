numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

num1 = numbers[0:4]
num2 = numbers[:4:-1]
num = num1 + num2 # извлечение значений списка для подсчета суммы без элемента None

summ = sum(num)
lenght = len(numbers)
average = round(summ / lenght, 2)

numbers[4] = average

print("Измененный список:", numbers)