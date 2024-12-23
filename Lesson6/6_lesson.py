    # Создайте модуль и напишите в нем функцию, которая получает на вход дату в формате DD.MM.YYYY. Функция возвращает истину, если дата может существовать и ложь, если невозможна. 
    # Для простоты договоримся, что год может быть в диапазоне [1, 9999]. Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
    # Проверку года на високосность внести в отдельную защищенную функцию.
    
from datetime import datetime as dt
from calendar import isleap

def check_date(date: str):
    try:
        t = dt.strptime(date, '%d.%m.%Y')
        _isleap(t.year)
        return True
    except:
        return False


def _isleap(year: int):
    print("Високосный" if isleap(year) else "Не високосный")
    
    
if __name__=='__main__':
    print(check_date("25.06.1984"))
    