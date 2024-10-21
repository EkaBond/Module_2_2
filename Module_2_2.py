first = input('Веедите первое число: ')
second = input('Введите второе число: ')
third = input('Введите третье число: ')
#if first == second ==third: #я написала так и вроде работает. Можно ли так? Прошу дать обратную связь.
#    print(3)
if first == second and first == third: #на всякий переписала, заодно попробовала и строгий оператор
    print(3)
elif first == second or first == third or second == third: #здесь не строгий, тк нужно либо/либо
    print(2)
# elif first != second or first != third or second != third:
#     print(0)
#сначала прописала третье условие, но поняла что:  1. тогда это больше работы
#                                                  2. использовала не все функции из урока
else:
    print (0)
