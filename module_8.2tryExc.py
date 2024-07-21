incorrect_data = 0
result = 0


def personal_sum(numbers):
    try:
        for i in numbers:
            global result
            result += i

    except TypeError:
        for i in numbers:
            global incorrect_data
            print(f'Некорректный тип данных для подсчёта суммы - {i}')
            incorrect_data += 1


    return (result, incorrect_data)


def calculate_average(numbers):
    try:
        sum = 0
        personal_sum(numbers)
        global result
        sum += result
        aver = sum / len(numbers)
        return aver
    except ZeroDivisionError as exc:
        return 0
    except TypeError:
        print('В numbers записан некорректный тип данных.')
        return None



# print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
# print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
# print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
# print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать
# print(f'Результат 5: {calculate_average([1, 2, 3, 4])}')
# personal_sum("1, 2, 3")
# personal_sum((1, '3', 5, 7))
