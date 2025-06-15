from Employe import Employee

class Manager(Employee):
    def __init__(self, name, age, job_title, salary, Team_Unit = 0):
        super().__init__(name, age, job_title, salary)
        self._Team_Unit = Team_Unit  

    def getDetails(self):
        if self._Team_Unit == 0 :
            return super().getDetails()
        else:
            return super().getDetails() + f"\nTeam_Unit : {self._Team_Unit}"
    def getWork(self):
        if self._Team_Unit == 0 :
            return super().getWork()
        else:
            return f"{self.name} Bekerja sebagai Manager dengan jumlah team {self._Team_Unit}"
