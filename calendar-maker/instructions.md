# Calendar Maker - Instructions

This program generates printable text files of monthly calendars for the month and year you enter. 

Dates and calendars are a tricky topic in programming because there are so many different rules for determining the number of days in a month, which years are leap years, and which day of the week a particular date falls on. 

Fortunately, Python’s `datetime` module handles these details for you. 

This program focuses on generating the multiline string for the monthly calendar page.

<br>

## The Program in Action

When you run _calendarmaker.py_, the output will look like this:

```
Calendar Maker, by Al Sweigart al@inventwithpython.com
Enter the year for the calendar:
> 2029
Enter the month for the calendar, 1-12:
> 12
                                  December 2029
...Sunday.....Monday....Tuesday...Wednesday...Thursday....Friday....Saturday..
+----------+----------+----------+----------+----------+----------+----------+
|25        |26        |27        |28        |29        |30        | 1        |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
+----------+----------+----------+----------+----------+----------+----------+
| 2        | 3        | 4        | 5        | 6        | 7        | 8        |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
+----------+----------+----------+----------+----------+----------+----------+
| 9        |10        |11        |12        |13        |14        |15        |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
+----------+----------+----------+----------+----------+----------+----------+
|16        |17        |18        |19        |20        |21        |22        |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
+----------+----------+----------+----------+----------+----------+----------+
|23        |24        |25        |26        |27        |28        |29        |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
+----------+----------+----------+----------+----------+----------+----------+
|30        |31        | 1        | 2        | 3        | 4        | 5        |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
+----------+----------+----------+----------+----------+----------+----------+

Saved to calendar_2029_12.txt
```

## How It Works

Note that the `getCalendarFor()` function returns a giant multiline string of the calendar for the given month and year. 

In this function, the `calText` variable stores this string, which adds the lines, spaces, and dates to it. 

To track the date, the `currentDate` variable holds a `datetime.date()` object, which gets set to the next or previous date by adding or subtracting `datetime.timedelta()` objects.