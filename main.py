#Программа для расчета налогов

#Функция расчэта суммы с начислением НДС 20%
def summa_nds20():
    request = input('Введите сумму до налога: ')
    nds20 = (int(request)/120)*20

    print(f'НДС от суммы {request} составит: {int(nds20)} руб.')

    summa_nds20 = int(request) + int(nds20)
    print(f'Общая сумма с НДС 20% составляет: {int(summa_nds20)} руб.')

#Функия расчёта суммы за вычитом НДС 20%
def minus_nds20():
    request = input('Введите сумму c налогом: ')
    nds20 = (int(request) / 120) * 20

    print(f'НДС от суммы {request} составит: {int(nds20)} руб.')

    minus_nds20 = int(request) - int(nds20)
    print(f'Cумма без НДС 20% составляет: {int(minus_nds20)} руб.')

#Вывод расчёта
def result():
    answer = input('Посчитать сумму ДО или БЕЗ НДС?: ').lower()
    if answer == 'до' or answer == 'lj':
        summa_nds20()
    else:
        minus_nds20()
result()

#Функция повторного запроса расчёта
def repeat():
    repeat = input('Расчитать ещё? (Да / Нет): ').lower()
    if repeat == 'да' or repeat == 'lf':
        result()
    else:
        print('До скорых встреч!')
repeat()
