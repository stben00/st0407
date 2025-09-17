print("Добро пожаловать в игру ~ Угадай число ~ ")
print("Настя загадывает число.  Дима, не подглядывай ")

nastya_number = int(input("Введите число: "))
dima_number = int(input("Угадывай число: "))

if dima_number == nastya_number:
    print("Дима угадал номер !")
else:
    print("Дима проиграл так как не угадал !")
    
    

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))


user_sum = int(input("Сумма этих чисел: "))

correct_sum = a + b

if user_sum == correct_sum:
    print("Ответ верный !")

else:
    print("Ответ не верный !")
    print("Правильный резулатат: ", correct_sum)