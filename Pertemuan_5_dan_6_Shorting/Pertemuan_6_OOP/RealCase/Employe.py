from Person import Person

class Employee(Person):
    def __init__(self, name, age, job_title, salary):
        super().__init__(name, age)
        self._job_title = job_title
        self._salary = salary

    def getDetails(self):
        return f"Name Employe: {self.name}\nAge: {self.getAge}\nJob Title: {self._job_title}\nSalary: {self._salary}"

    def getWork(self):
        return f"{self.name} hanya seorang employee"