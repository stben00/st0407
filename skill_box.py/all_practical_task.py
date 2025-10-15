#Пример (1) 
#Вывести числа от 0 до 4 : 

for i in  range(4):
    print(i)
    


#Пример (2) 
#Задать Диапазон от 1 до 6  

for i in range(1,6):
    print(i)


#Пример (3). 
#С шагом ( через сколькот прибавлять )

for i in range (0, 10, 2):
    print(i)



#Пример (4)
#Обратный отчет 

for i in range(10, 0, -1 ):
    print(i)



#Пример (5)
#Повторяем Фразу !

for i in range (3):
    print(" Я учу Python !")

for i in range(1, 6):
    print("*" * i)

for i in range(1, 11):
    print(f"9 × {i} = {9 * i}")
    
for i in range(1,11):
    print(f"5 x {i} = { 5 * i } ")
    
for i in range(1, 11):
    print(f"3 x {i} = { 3 * i }")
    
number = int(input("Введите число, для которого нужно таблица: "))

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}" )

number = int(input("Введите число: "))
while number >= 0:
    if number == 3 or number == 1 or number == 4:
        number -= 1
        continue 
    print(number)
    number -= 1
    

n = int(input("Введите число N : "))
i = 2
while i <= n:
    print(f"{i} ** 3 = {i ** 3}")
    i += 1
    

    
    
Q = int(input("Ввемдте число Q: "))
i = 1
while i <= Q:
    print(f"{i} * 5 = {i * 5}")
    i += 1
    
    
    
    
n = int(input("Введите число (>= 0): "))
while n < 0:
    n = int(input("Введите НЕОТРИЦАТЕЛЬНОЕ  число: "))

if n == 0:
    count = 1
else:
    count = 0
    while n > 0:
        n //= 10
        count += 1
        
print("Кол - во цифр в числе: ", count)
    
    
print("Начался восьмичасовой работчий день. ")

total_tasks = 0 
answered_once = False

hour = 1

while hour <= 8:
    print(f"{hour} - й час ")
    tasks = int(input("Сколько задач решил Максим: "))
    total_tasks += tasks
    
    if not answered_once:
        take_call = int(input("Зваонит жена. Взять трубку ? ( 1- да, 0- нет ):"))
        if take_call == 1:
            answered_once = True
            
    
    hour += 1 

print("\nРабочий день закончился. Всего выполнено заданий: ", total_tasks)
if answered_once:
    print("Нужно зайти в магазин! ")

