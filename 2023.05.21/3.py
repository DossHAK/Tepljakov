minutes = int(input('Введите количество минут: '))
# УДАЛИТЬ: данные переменные используются каждая только единожды — неоптимально
# КОММЕНТАРИЙ: если бы операции, выполняемые для вычисления значений этих переменных, были бы более сложными и длинными, то можно было оправдать создание отдельных переменных — в данном случае операции тривиальны и вполне могут быть прописаны и выполнены вместо использования данных переменных (как вы сделали в предыдущей задаче)

# Исправил как понял
# hour = minutes // 60
# minute = minutes % 60
# print(f'{minutes} мин - это {hour} час {minute} мин')

print(f'{minutes} мин - это {minutes // 60} час {minutes % 60} мин')


# Введите количество минут: 150
# 150 мин - это 2 час 30 мин


# ИТОГ: хорошо, но можно лучше — 2/3
