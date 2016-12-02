import random


# Генератор вычленения полей из массива словарей
def field(items, *args):

    for n in items:
        if len(args) == 1:
            if  n.get(args[0]):
                yield n.get(args[0])
        else:
            new_items = {}
            for x in args:
                if n.get(x):
                    new_items[x] = n[x]

            if len(new_items) > 0:
                yield new_items


# Генератор списка случайных чисел
def gen_random(begin, end, num_count):
    a = 0
    while a < num_count:
        yield random.randint(begin,end)
        a += 1
