from enum import Enum
import math

class Week (Enum):
    Monday = ('понедельник', 1)
    Tuesday = ('вторник', 2)
    Wednesday = ('среда', 3)
    Thursday = ('четверг', 4)
    Friday = ('пятница', 5)
    Saturday = ('суббота', 6)
    Sunday = ('воскресенье', 7)

    def __init__(self, day, num):
        self.day = day
        self.num = num

def calculate_day (weekday):
    list_day = [Week.Monday, Week.Tuesday, Week.Wednesday, Week.Thursday, Week.Friday, Week.Saturday, Week.Sunday]
    weekday = weekday.lower()

    if weekday == Week.Saturday.value[0]:
        return Week.Sunday.value[1] - Week.Saturday.value[1]

    elif weekday == Week.Sunday.value[0]:
        return 6

    for day in list_day:
        if day.value[0] == weekday:
            return Week.Saturday.value[1] - day.value[1]

if __name__ == '__main__':
    print(calculate_day('суббота'))
    print(calculate_day('среДа'))
    print(calculate_day('ВоСкРеСеНьЕ'))
