i = 0
g = 0
l = 0
c = 0
n = 0
# Удаление отриц. чисел
x = [1, 3, 5, -1, 3, -2]
for i in range(len(x)-1):
    if x[i] < 0:
        del x[i]
print(x)

# Посчитать отрицательные числа
y = [[1, -1, 0], [2, 5, -9], [-2, -3, 0]]
for g, l in enumerate(y):
    for c, k in enumerate(l):
        if k < 0:
            n += 1
print(n)

# Генератор, возвращающий нечет числа
for num in range(100):
    if num%2 != 0:
        print(num)

# Словарь, содержащий числа и их кубы
slovar = {}
for num in range(11, 15):
    slovar[num] = num**2
print(slovar)

# Программа в 8 модуле(упрощение+улучшение)
char = 0
words = 0
line = open('C:\\Users\\Student\\Desktop\\word_count.txt').read()
lines = len(line.split("\n"))
words += len(line.split())
chars = line.translate(str.maketrans(",.!?", "    "))
for ch in chars:
    if ch != " ":
        char += 1
print("File has {0} lines, {1} words, {2} characters".format(lines, words, char))