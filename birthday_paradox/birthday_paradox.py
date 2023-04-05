"""
Birthday Paradox Simulation
"""

import datetime
import calendar
import random


def random_birthday() -> datetime.date:
    year = datetime.date.today().year
    total_days = 365 if calendar.isleap(year) else 364
    nth_day = random.randint(0, total_days)
    return datetime.date(year, 1, 1) + datetime.timedelta(days=nth_day)


def generate_birthdays(n: int) -> list[datetime.date]:
    return [random_birthday() for _ in range(n)]
