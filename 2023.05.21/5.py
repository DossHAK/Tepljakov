whole, fraction = int(input('Введите целую часть мили: ')), int(input('Введите дробную часть мили: '))
# Введите целую часть мили: 15
# Введите дробную часть мили: 7
miles = float(f'{whole}.{fraction}')
# Задаем конструкцию числа Миля
km = (f'{miles * 1.61:.1f}')
# Высчитываем количество киллометров в миле
print(f'{miles} миль = {km} км')


# Результат
# 15.7 миль = 25.3 км