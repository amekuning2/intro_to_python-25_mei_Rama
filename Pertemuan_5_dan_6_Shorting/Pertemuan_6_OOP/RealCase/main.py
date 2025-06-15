from Manager import Manager

def main():
    list_data = [
        {
            "name": "Rama Prasetia",
            "age": 35,
            "job_title": "Software Engineer",
            "salary": 70000,
            "team_unit": 0
        },
        {
            "name": "Ame",
            "age": 30,
            "job_title": "Design Engineer",
            "salary": 60000,
            "team_unit": 1
        },
        {
            "name": "Budi",
            "age": 40,
            "job_title": "Project Manager",
            "salary": 90000,
            "team_unit": 5
        }
    ]
    print("=== Detail Employee ===")
    for person in list_data:
        print("=== Profile ===")
        Employee = Manager(person['name'],person['age'],person['job_title'],person["salary"],person["team_unit"])
        print(Employee.getDetails())
        print('====== Detail Job ======')
        print(Employee.getWork())

if __name__ == "__main__":
    main()