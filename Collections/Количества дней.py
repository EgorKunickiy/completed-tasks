import math

def calculate_day (weekday: str) ->int:
    weekday = weekday.lower()
    list_days = dict([
                    ('понедельник', 1),
                    ('вторник', 2),
                    ('среда', 3),
                    ('четверг', 4),
                    ('пятница', 5),
                    ('суббота', 6),
                    ('воскресенье', 7)])
    if weekday == 'суббота':
        return list_days['воскресенье'] - list_days['суббота']

    elif weekday == 'воскресенье':
        return 6

    else:
        return list_days['суббота'] - list_days[weekday]

if __name__ == '__main__':
    print(calculate_day('суббота'))
    print(calculate_day('среДа'))
    print(calculate_day('ВоСкРеСеНьЕ'))
