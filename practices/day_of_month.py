import calendar


def get_day_of_month(y, m):
  return calendar.monthrange(y, m)[1]


if __name__ == "__main__":
  try:
    year = int(input("Enter a year: "))
    month = int(input("Enter a month: "))
    print(get_day_of_month(year, month))
  except ValueError:
    print("Please enter a valid year and month")
