"""
• Type in the dataclass code from the previous slide
• Add one more field: gpa, a float
• Write a main function to create some example Student objects
• Compare the dataclass version to the "traditional" version
"""

from dataclasses import dataclass
@dataclass

class Student:
  # this is much cleaner than the traditional version.
  name: str
  school_id: str
  gpa: float

  def __str__(self):
    return f'Name: {self.name:<8} | ID: {self.school_id:<8} | GPA: {self.gpa:<8}'

def main():
  alex = Student('Alex', '12345', 3.4)
  print(alex)

  sam = Student('Sam', '64565', 3.2)
  print(sam)

  john = Student('John', '96654', 3.8)
  print(john)

if __name__ == '__main__':
  main()