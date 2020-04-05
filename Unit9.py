import time
from datetime import time, datetime
import time

class Time:
    def __init__(self, index, encoding='utf-8'):
        self.file = open(index, 'a', encoding=encoding)


    def __enter__(self):
        self.start_time = time.time()
        self.write(f'Начало работы {self.start_time}\n')
        self.now = datetime.now()
        print(f'Начало работы программы {self.start_time}\n')
        self.name = input("Введи свое имя")
        self.write(f'Пользователь {self.name} ({self.now})\n')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        distinction_time = abs(self.start_time - time.time())
        if exc_type is not None:
            print(exc_type)
            self.write(f'error: {exc_val}')
        print(f'Окончание работы программы {time.time()}\n')
        self.write(f'Окончание работы {time.time()}\n')
        print(f'Программа работала {distinction_time} секунд')
        self.write(f'Программа работала {distinction_time} секунд')

    def age(self):

        try:
            self.year = int(input("Введите год"))
            self.month = int(input("Введите месяц"))
            self.day = int(input("Введите день"))
            self.deadline = datetime(self.year, self.month, self.day)
            if self.deadline > self.now:
                print("Ты еще не родился")
                self.write(f'Ты еще не родился\n')
                self.life = None
            else:
                life = self.now - self.deadline
                self.life = life
                print("Ты живешь","{} дней  {} секунд   {} микросекунд".format(life.days, life.seconds, life.microseconds))
                self.write(f'Ты уже живешь {self.life.days} дней\n')
            return self.life
        except ValueError or AttributeError:
            print("Ошибочный ввод даты")



    def write(self, fixed):
        self.file.write(f'{datetime.now()}    {fixed}\n')



print("Посчитаем, сколько дней ты живешь")

with Time('unit.txt') as f:
    f.age()