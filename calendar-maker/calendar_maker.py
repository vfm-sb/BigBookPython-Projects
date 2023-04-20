"""
Simplified Version of Calendar Maker, Version 0
"""

__version__ = "0.1.0"

import calendar


def get_year() -> int:
    while True:
        print("Enter The Year for The Calendar:")
        try:
            year_input = input("> ")
            if not year_input.isdecimal():
                raise ValueError(
                    "Invalid Input!"
                    "Input Value Must Be a Decimal Value."
                )
            year = int(year_input)
            if not 0 <= year <= 9999:
                raise ValueError(
                    "Invalid Year!"
                    "Input Value Must Be Between 0 and 9999 (Inclusive)."
                )
            break
        except ValueError as error_message:
            print(error_message)
            print("Please Try Again!")
    return year


def get_month() -> int:
    while True:
        print("Enter The Month for The Calendar, 1-12:")
        try:
            month_input = input("> ")
            if not month_input.isdecimal():
                raise ValueError(
                    "Invalid Input!"
                    "Input Value Must Be a Decimal Value."
                )
            month = int(month_input)
            if not 1 <= month <= 12:
                raise ValueError(
                    "Invalid Month!"
                    "Input Value Must Be Between 1 and 12 (Inclusive)."
                )
            break
        except ValueError as error_message:
            print(error_message)
            print("Please Try Again!")
    return month


def cli_calendar_maker() -> None:
    print(f"Simplified Version of Calendar Maker by VFM/SB, (Version {__version__})")
    year = get_year()
    month = get_month()
    custom_calendar = calendar.TextCalendar()
    custom_calendar.prmonth(year, month, w=8, l=3)


def main() -> None:
    cli_calendar_maker()


if __name__ == "__main__":
    main()
