import random


def get_numbers_ticket(min, max, quantity):
    if min >= 1 and max <= 1000:
        if min <= quantity <= max:
            numbers = [random.randint(min, max) for i in range(min, max+1)]  # генеруемо список
            unique_numbers = set(numbers)  # робимо унікальні значення
            unique_numbers_lst = list(unique_numbers)  # робимо список унікальних значень
            result = random.sample(unique_numbers_lst, k=quantity)
            return sorted(result)  # сортуемо
        else:
            return list()

    return list()


lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
