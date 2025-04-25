num = input("Enter a number: ")


def print_asterisk(n):
  try:
    n = int(n)
    print("*" * n)
  except ValueError:
    print("Please enter a valid number")


if __name__ == '__main__':
  print_asterisk(num)
