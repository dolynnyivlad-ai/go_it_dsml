import random


def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000:
        return list()
    elif min > max:
        return list()
    elif quantity <= 0 or quantity > (max - min + 1):
        return list()

    else:
        numbers = [random.randint(min, max) for i in range(min, max + 1)]  # генеруемо список
        unique_numbers = set(numbers)  # робимо унікальні значення
        unique_numbers_lst = list(unique_numbers)  # робимо список унікальних значень
        result = random.sample(unique_numbers_lst, k=quantity)
        return sorted(result)  # сортуемо


lottery_numbers = get_numbers_ticket(10, 14, 6)
print("Ваші лотерейні числа:", lottery_numbers)
