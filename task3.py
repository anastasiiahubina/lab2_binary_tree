# Відображення операцій у відповідні букви прав
operation_map = {
    'read': 'R',
    'write': 'W',
    'execute': 'X'
}

# Зчитування вхідних даних
n = int(input())
permissions = {}

# Зчитуємо права доступу до кожного файлу
for _ in range(n):
    parts = input().split()
    filename = parts[0]
    rights = set(parts[1:])
    permissions[filename] = rights

# Зчитування кількості запитів
m = int(input())

# Обробка кожного запиту
for _ in range(m):
    op, filename = input().split()
    if operation_map[op] in permissions.get(filename, set()):
        print("OK")
    else:
        print("Access denied")