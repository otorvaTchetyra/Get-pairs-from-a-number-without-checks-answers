def find_pairs(n):
    pairs = []
    for i in range(1, n):
        for j in range(i + 1, n):
            if n % (i + j) == 0:
                pairs.append((i, j))
    return pairs

n = int(input("Введите число от 3 до 20: "))
result = find_pairs(n)
print("Пароль: ", end=' ')
for pair in result:
    print(pair[0], pair[1], end=' ')