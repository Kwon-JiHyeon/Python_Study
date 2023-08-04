class Person:
    def __init__(self, name, phone=None):
        self.name = name
        self.phone = phone

    def __repr__(self):
        return f'<Person {self.name}, {self.phone}>'

  # Person 클래스 상속받는 Employee 클래스
  class Employee(Person):
    def __init__(self, name, phone, position, salary):
        #Person.__init__(self, name, phone)
        #super(Employee, self).__init__(name, phone)
        super().__init__(name, phone)
        self.position = position
        self.salary = salary
