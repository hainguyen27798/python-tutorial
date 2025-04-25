num = input("Enter a number: ")


def multiple_by_2(n):
  try:
    n = int(n)
    print(n * 2)
  except ValueError:
    print("Please enter a valid number")


if __name__ == "__main__":
  multiple_by_2(num)
