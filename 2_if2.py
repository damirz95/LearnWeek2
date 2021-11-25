"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    def f_vs_s(first_string, second_string):
      if type(first_string) == str and type(second_string) == str:
        if len(first_string) == len(second_string):
          print('1')
        elif len(first_string) > len(second_string):
          print('2')
        elif len(first_string) != len(second_string) and second_string == 'learn':
          print('3')
        else:
          print('error')
      else:
        print('0')    

    f_vs_s(0 , 'second')
    f_vs_s('second', 'second')
    f_vs_s('00', '1')
    f_vs_s('0', 'learn')




if __name__ == "__main__":
    main()
