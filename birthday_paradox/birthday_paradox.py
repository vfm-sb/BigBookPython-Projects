"""
Birthday Paradox Simulation
"""

import datetime
import calendar
import random


def random_date() -> datetime.date:
    year = datetime.date.today().year
    total_days = 365 if calendar.isleap(year) else 364
    nth_day = random.randint(0, total_days)
    return datetime.date(year, 1, 1) + datetime.timedelta(days=nth_day)


def generate_random_dates(n: int) -> list[datetime.date]:
    return [random_date() for _ in range(n)]


def has_duplicate_dates(dates: list[datetime.date]) -> bool:
    return len(dates) == len(set(dates))


def matching_dates(birthdays: list[datetime.date]) -> list[datetime.date]:
    unique_birthdays = []
    common_birthdays = []
    for birthday in birthdays:
        if birthday in unique_birthdays:
            common_birthdays.append(birthday)
        else:
            unique_birthdays.append(birthday)
    return common_birthdays
