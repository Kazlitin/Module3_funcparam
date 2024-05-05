def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params(1, 'строка', True)

def print_params(*args):
    for arg in args:
        print(arg)

# Вызов функции без аргументов
print_params()

# Вызов функции с несколькими аргументами
print_params('Один', 'Два', 'Три')

def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params(b = 25)
print_params(c = [1, 2, 3])

#распаковка параметров
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
values_list = [1, 'string', [1, 2, 3]]
values_dict = {'a': 1, 'b': 'строка', 'c': True}


print_params(*values_list)
print_params(**values_dict)


def print_params(*args):
    pass
print()

values_list2 = [[1, 3, 5], 'список']
print_params(*values_list2,42)




