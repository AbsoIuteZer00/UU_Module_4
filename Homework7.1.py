file_name = 'poems.txt'
with open(file_name, mode='r') as file:
    for line in file:
        print(line, end='')

# Опертаор with контролирует вход в блок кода и выход из него. При выходе из блока кода закрывает его самостоятельно.
