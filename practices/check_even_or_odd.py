num = input("Enter a number: ")


def check_even_or_odd(n):
  try:
    n = int(n)
    if n % 2 == 0:
      print("Even")
    else:
      print("Odd")
  except ValueError:
    print("Please enter a valid number")


if __name__ == "__main__":
  check_even_or_odd(num)
