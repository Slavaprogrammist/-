# Книга, Книжный магазин

from operator import itemgetter

class Kniga:
    """Книга"""

    def __init__(self, id, naz, stoim, mag_id):
        self.id = id
        self.naz = naz # название
        self.stoim = stoim # стоимость
        self.mag_id = mag_id

class Knizhnimagazin:
    """Книжный магазин"""

    def __init__(self, id, name):
        self.id = id
        self.name = name

class Knigavmagazine:
    """Книга в магазине для реализации связи многие-ко-многим"""

    def __init__(self, kniga_id, magazin_id):
        self.kniga_id = kniga_id
        self.magazin_id = magazin_id

# Магазин
magazin = [
    Knizhnimagazin(1, 'Для малышей'),
    Knizhnimagazin(2, 'Современник'),
    Knizhnimagazin(3, 'Для школьников и их родителей'),
    Knizhnimagazin(4, 'Книга - друг человека'),
    Knizhnimagazin(5, 'Зарубежные книги'),
    Knizhnimagazin(6, 'Литература о саморазвитии'),
]

# Книга
knigi = [
    Kniga(1, 'Алфавит', 500, 1),
    Kniga(2, 'Приключения Тома Сойера', 2000, 5),
    Kniga(3, 'Магия утра', 2500, 6),
    Kniga(4, 'Красота мира', 450, 2),
    Kniga(5, 'Капитанская дочка', 3000, 4),
    Kniga(6, 'Алиса в стране чудес', 200, 2),
]

knigiandmagazin = [
    Knigavmagazine(1, 4),
    Knigavmagazine(2, 6),
    Knigavmagazine(3, 4),
    Knigavmagazine(3, 3),
    Knigavmagazine(1, 1),
    Knigavmagazine(2, 1),
    Knigavmagazine(5, 2),
    Knigavmagazine(6, 3),
    Knigavmagazine(4, 5),
    Knigavmagazine(4, 4),
]

def main():
    """Основная функция"""

    # Соединение данных один-ко-многим
    one_to_many = [(k.naz, k.stoim, m.name)
                   for m in magazin
                   for k in knigi
                   if k.mag_id == m.id]

    # Соединение данных многие-ко-многим
    many_to_many_temp = [(m.name, km.magazin_id, km.kniga_id)
                         for m in magazin
                         for km in knigiandmagazin
                         if m.id == km.magazin_id]

    many_to_many = [(k.naz, k.stoim, Knizhnimagazin_name)
                    for Knizhnimagazin_name, magazin_id, kniga_id in many_to_many_temp
                    for k in knigi if k.id == kniga_id]

    print('Задание В1')
    res1 = []
    for naz, stoim, Knizhnimagazin_name in one_to_many:
        if 'А' in naz[0]:
            res1.append((naz, Knizhnimagazin_name))
    print(res1)

    print('Задание В2')
    buff = []
    for a in magazin:
        magmin = list(filter(lambda i: i[2] == a.name, one_to_many))
        if len(magmin) > 0:
            a_stoim = [stoim for _, stoim, _ in magmin]
            min_stoim = min(a_stoim)
            buff.append((a.name, min_stoim))
    res2 = sorted(buff, key=itemgetter(1))
    print(res2)

    print('Задание В3')
    buff = []
    for naz, stoim, Knizhnimagazin_name in many_to_many:
        buff.append((naz, Knizhnimagazin_name))
    res3 = list(sorted(buff, key=itemgetter(0)))
    print(res3)

if __name__ == '__main__':
    main()