import csv


class Student:
  def __init__(self, name, maths, literality, english):
    self.name = name
    self.maths = maths
    self.literality = literality
    self.english = english

  def average(self):
    return (self.maths + self.literality + self.english) / 3

  def academic_standing(self):
    average = self.average()
    if average >= 85:
      return "Excellent"
    elif average >= 70:
      return "Good"
    elif average >= 55:
      return "Average"
    elif average >= 40:
      return "Below Average"
    else:
      return "Fail"


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
  print(f"{'Name':<20} {'Average':>8} {'Academic Standing':>20}")
  print("-" * 50)
  for student in students:
    print("{name:<20} {average:>8.2f} {academic_standing:>20}".format(name=student.name, average=student.average(),
                                                                      academic_standing=student.academic_standing()))
