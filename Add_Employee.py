class AddEmployeeManually():
    def __init__(self, name, id, age, phone):
        self.name = name
        self.phone = phone
        self.age = age
        self.id = id

    def setData(self):
        with open('Employees.txt', 'a') as employees:
            try:
                employees.write(self.id)
                employees.write('\t')
                employees.write(self.name)
                employees.write('\t')
                employees.write(self.phone)
                employees.write('\t')
                employees.write(self.age)
                employees.write('\n')
            except:
                print('No Data entered yet!')

class AddEmployeeFromFile():
    def appendEmployees(self,new_employees_file):
        with open('Employees.txt', 'a') as employees:
            try:
                new_employees = open(new_employees_file, 'r')
            except:
                print("No such file exists")
            else:
                if new_employees.read():
                    employees.write(new_employees.read())
                else:
                    print('File is empty! Nothing to add.')
