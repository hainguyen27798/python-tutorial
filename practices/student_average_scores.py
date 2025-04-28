import csv


class Student:
  def __init__(self, name, maths, literality, english):
    self.name = name
    self.maths = maths
    self.literality = literality
    self.english = english

  def average(self):
    return (self.maths + self.literality + self.english) / 3


def read_csv(filename):
  student_list = []
  try:
    with open(filename, 'r') as f:
      reader = csv.reader(f)
      reader.__next__()
      for row in reader:
        student_list.append(Student(row[0], float(row[1]), float(row[2]), float(row[3])))
  except FileNotFoundError:
    print("File not found")
    exit()
  return student_list


if __name__ == '__main__':
  students = read_csv('../data/student-subject-scores.csv')
  print(f"{'Name':<20} {'Average':>8}")
  print("-" * 30)
  for student in students:
    print("{name:<20} {average:>8.2f}".format(name=student.name, average=student.average()))
