class Employee:
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary
        self.email = first + "." + last + "@company.com"
        if salary == 0:
            print("Onko tämä harjoittelija?")
            print(self.fullname())
    def fullname(self):
        return "{} {}".format(self.first, self.last)


emp_1 = Employee("Anna", "Mäki", 0)
print(emp_1.email)
print(emp_1.fullname())