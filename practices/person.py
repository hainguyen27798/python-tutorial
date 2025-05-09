class Person:
  def __init__(self, name: str, surname: str, address: str):
    self.name = name
    self.surname = surname
    self.address = address


class Student(Person):
  def __init__(self, name: str, surname: str, address: str, source: list[str]):
    super().__init__(name, surname, address)
    self.source = source


class Teacher(Person):
  def __init__(self, name: str, surname: str, address: str, salary: float):
    super().__init__(name, surname, address)
    self.salary = salary


if __name__ == '__main__':
  st = Student("John", "Doe", "123 Main St", ["Math", "Science"])
  print(st.name)
