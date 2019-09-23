import csv
import random
import string
import Add_Employee
import Delete_Employee
import Attendance

"""
Note* this program is for a company with 90 employees max due to the auto generated id
Otherwise the code for ID needs to be upgraded to more then 2 digit number
"""
#this function is to check if auto generated id already exists in Employees file
def id_exists(id):
    with open('Employees.txt', 'r') as employees:
        lines = employees.readlines()
        id_exist = True
        for line in lines:
            if id not in line.split("\t")[0]:
                id_exist = False
    return id_exist

def main():
    choice = int(input("Please type: \n 1 to Add Employee Manually, "
                       "\n 2 to Add from file, "
                       "\n 3 to Delete Employee Manually and "
                       "\n 4 to Delete Employee from File and "
                       "\n 5 to ClockIn and "
                       "\n 6 to Generate Attendance Report "
                       "\n 7 to Generate Current Moth Attendance Report and "
                       "\n 8 to Generate Lateness Report: \n"))
    if choice == 1:
        name = str(input('Enter Employee name:'))
        #id = input('Enter Employee id:')
        # randomly generated id number length of 2 digits
        id = ''.join(random.choice(string.digits) for _ in range(2))
        # regenerate if exists checking if exists already:
        #count is to make sure if the id numbers reach 99 it will not enter endless loop
        count = 10
        while id_exists(id) == True or count <= 99:
            # randomly generated id number length of 2 digits
            id = ''.join(random.choice(string.digits) for _ in range(2))
            count += 1

        phone = input('Enter Employee phone number:')
        #validating phone number input
        try:
            phone_val = int(phone)
        except ValueError:
            print("Phone number must consist of digits only.")
        else:
            age = input('Enter employee age:')
            #validating age input
            try:
                age_val = int(age)
            except ValueError:
                print("Age input must be an intiger!")
            else:
                employee = Add_Employee.AddEmployeeManually(name,id,phone,age)
                employee.setData()
    elif choice == 2:
        new_employees_file = input('enter filename with extention:')
        employee = Add_Employee.AddEmployeeFromFile()
        employee.appendEmployees(new_employees_file)
    elif choice == 3:
        employee_id = input('Enter existing Employee to be deleted:')
        delete_employee = Delete_Employee.DeleteEmployeeManually()
        delete_employee.deleteEmployee(employee_id)
    elif choice == 4:
        delete_employee_file = input('enter filename with extention if any:')
        delete_employee = Delete_Employee.DeleteEmployeeFromFile()
        delete_employee.deleteEmployeeFile(delete_employee_file)
    elif choice == 5:
        id = input('Enter your Employee ID number:')
        clockIn_employee = Attendance.ClockIn()
        clockIn_employee.checkExistance(id)
    elif choice == 6:
        id = input('Enter Employee ID to Generate Report:')
        employee = Attendance.AttendanceReport()
        employee.report(id)
    elif choice == 7:
        currentMonthReport = Attendance.CurrentMonthReport()
        currentMonthReport.report()
    elif choice == 8:
        employee = Attendance.LatenessReport()
        employee.isLate()
    else:
        print ("Not correct choice!")
if __name__ == "__main__":
    main()