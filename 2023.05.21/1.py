# КОММЕНТАРИЙ: непосредственно в коде размещайте комментарии, относящиеся к реализации, а не выполнению: PEP 8 рекомендует размещать комментарий непосредственно над комментируемой строчкой кода (это общепринятая практика в написании кода на самых разных языках)
#  https://peps.python.org/pep-0008/

name = input('Ввелите своё имя: ')
surname = input('Введите свою фамилию: ')
year = int(input('Введите свой год рождения: '))
age = 2023 - year
# ИСПРАВИТЬ: стоит попробовать справиться за один вызов print()
print(surname, name, end=', ')
print(age)


# КОММЕНТАРИЙ: а результат выполнения целиком размещайте после кода — в дальнейшем вам понадобится запускать и выполнять приложение несколько раз с разными входными данными, и результаты таких выполнений размещайте один под другим, например:
# Ввелите своё имя: Владислав
# Введите свою фамилию: Тепляков
# Введите свой год рождения: 1992
# Тепляков Владислав, 31

# Ввелите своё имя: Геннадий
# Введите свою фамилию: Шаповаленко
# Введите свой год рождения: 1992
# Шаповаленко Геннадий, 31


# ИТОГ: хорошо, но можно лучше — 2/3
