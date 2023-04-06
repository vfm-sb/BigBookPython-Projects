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


def str_dates(dates: list[datetime.date]) -> list[str]:
    return [date.strftime("%B %e") for date in dates]


def print_dates(str_dates: list[str]) -> None:
    for counter, date in enumerate(str_dates, start=1):
        print(date, end=", ")
        if counter % 10 == 0:
            print()


def birthday_simulator():
    print("Birthday Paradox...")
    print("How Many Birthdays To Be Generated? (Max 100)")
    while True:
        try:
            number_of_birthdays = input("> ")
            if not number_of_birthdays.isdigit():
                raise ValueError("Input Must Be a Positive Integer!")
            number_of_birthdays = int(number_of_birthdays)
            if 1 <= number_of_birthdays <= 100:
                raise ValueError("Number is Out of Range (1-100).")
            break
        except ValueError as error:
            print(error)
            print("Please Try Again!")
    # generate given number of birthdays
    random_birthdays = generate_random_dates(number_of_birthdays)
    print(f"Here are {len(random_birthdays)} Birthdays:")
    print_dates(str_dates(random_birthdays))
    