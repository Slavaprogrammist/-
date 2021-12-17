import unittest
import sys, os

sys.path.append(os.getcwd())
from main import *


class Test_task_1(unittest.TestCase):
    def test_task_1(self):
        one_to_many = [(k.naz, k.stoim, m.name)
                       for m in magazin
                       for k in knigi
                       if k.mag_id == m.id]
        self.assertEqual(Task1(one_to_many), [('Алфавит', 'Для малышей'), ('Алиса в стране чудес', 'Современник')])

class Test_task_2(unittest.TestCase):
    def test_task_2(self):
        one_to_many = [(k.naz, k.stoim, m.name)
                       for m in magazin
                       for k in knigi
                       if k.mag_id == m.id]
        self.assertEqual(Task2(one_to_many), [('Современник', 200), ('Для малышей', 500),
                                              ('Зарубежные книги', 2000), ('Литература о саморазвитии', 2500),
                                              ('Книга - друг человека', 3000)])


class Test_task_3(unittest.TestCase):
    def test_task_3(self):
        many_to_many_temp = [(m.name, km.magazin_id, km.kniga_id)
                             for m in magazin
                             for km in knigiandmagazin
                             if m.id == km.magazin_id]
        many_to_many = [(k.naz, k.stoim, Knizhnimagazin_name)
                        for Knizhnimagazin_name, magazin_id, kniga_id in many_to_many_temp
                        for k in knigi if k.id == kniga_id]
        self.assertEqual(Task3(many_to_many), [('Алиса в стране чудес', 'Для школьников и их родителей'),
                                               ('Алфавит', 'Для малышей'), ('Алфавит', 'Книга - друг человека'),
                                               ('Капитанская дочка', 'Современник'),
                                               ('Красота мира', 'Книга - друг человека'),
                                               ('Красота мира', 'Зарубежные книги'),
                                               ('Магия утра', 'Для школьников и их родителей'),
                                               ('Магия утра', 'Книга - друг человека'),
                                               ('Приключения Тома Сойера', 'Для малышей'),
                                               ('Приключения Тома Сойера', 'Литература о саморазвитии')])
if __name__ == "__main__":
    unittest.main()