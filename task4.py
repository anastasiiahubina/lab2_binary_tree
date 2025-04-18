# Зчитування вхідних даних
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

# Злиття двох відсортованих списків
result = []
i = j = 0

while i < n and j < m:
    if a[i] <= b[j]:
        result.append(a[i])
        i += 1
    else:
        result.append(b[j])
        j += 1

# Додаємо залишки з одного з масивів
result.extend(a[i:])
result.extend(b[j:])

# Вивід результату
print(*result)