                           ### 6.5 Цикл while со счётчиком #####

bags = int(input("Сколько мешков нужно перетащить: "))
totalWeigth = 0
bags_count = 0

while bags_count < bags:
    weigth = int(input("Сколько весит мешок: "))
    totalWeigth += weigth
    bags_count += 1

    print(f"Перетащили мешков {bags_count} из {bags}")
print(f"Общий вес {totalWeigth}")


secret_password = 123
attempts = 0
max_attempts = 3

while  attempts < max_attempts:

    try:

    
        password = int(input("Введите пожалуйста свой пароль: "))
        if secret_password == password:
            print("Добро Пожаловать !")
            break
        else:
            print(f"Ошибка !Попробуй еще попытка {attempts} из {max_attempts} ")
            attempts += 1
    
    except ValueError:
        print(f"Используйте только цифры ! Попытка {attempts}  из {max_attempts} ")
        attempts += 1



if attempts == max_attempts:
    print("Вы уже достаточно использвовали свои шансы ")
    
lines = int(input("Сколько раз вывести : "))
count = 0 

while count < lines:
    print("Я Програмист! ")
    count += 1
    


remainder = int(input("Сколько раз напонить ? "))
count = 0

while remainder > count:
    print("ВЫ ХОТЕЛИ НЕ ЗАБЫТЬ О ЧЕМ - ТО ")
    count += 1


    