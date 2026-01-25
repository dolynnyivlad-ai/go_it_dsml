from datetime import datetime, timedelta, date


def get_days_from_today(date: str):
    """
    Рекомендації для виконання:
    Розрахуйте різницю між поточною датою та заданою датою.

    Приклад:
    Якщо сьогодні 5 травня 2021 року, виклик get_days_from_today("2021-10-09") повинен повернути 157,
    оскільки 9 жовтня 2021 року є на 157 днів пізніше від 5 травня 2021 року.

    !!! Рекомендацыя НЕ співпадає з прикдадом!!! Я зробив функцыю за рекомендацією !!!
    """

    try:
        normalized_date = date.replace('.', '-').replace('/','-')
        convert_str_to_date = datetime.strptime(normalized_date, '%Y-%m-%d').date()
        today = datetime.today().date()
        diffence_days_btw_two_days = (today - convert_str_to_date).days
        return diffence_days_btw_two_days

    except ValueError as e:
        print(f'Date parsing error: {e}')
        print(f'Invalid date format "{date}". Expected: "YYYY.MM.DD", "YYYY/MM/DD" or "YYYY-MM-DD"')
        return print(f'today: {datetime.today().date()}, target day: {None}')

    except TypeError as e:
        print(f'Type parsing error: {e}')
        return print(f'today: {datetime.today().date()}, target day: {None}')

    except Exception as e:
        print(f'Unexpected parsing error: {e}')
        return print(f'today: {datetime.today().date()}, target day: {None}')


# for Testing

date_str = '20260301'
result = get_days_from_today(date_str)
print(result, type(result))

