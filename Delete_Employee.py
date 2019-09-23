class DeleteEmployeeManually():
    def deleteEmployee(self, employee_id):
        with open('Employees.txt', 'r') as employees:
            lines = employees.readlines()
        with open('Employees.txt', 'w') as employees:
            for line in lines:
                #line.split("\t")[0] the element before the first tab (id)
                if line.split("\t")[0] != employee_id:
                    employees.write(line)

class DeleteEmployeeFromFile():
    def deleteEmployeeFile(self,delete_employee_file):
        #reading from file with list of employees to be deleted
        delete_employee = open(delete_employee_file, 'r')
        lines = delete_employee.readlines()
        #creating a delete list
        delete_list = []
        #going thought a file lines to be deleted and adding id to a delete list
        for line in lines:
            if line.split("\t")[0]:
                delete_list.append(line.split("\t")[0])
        #if delete list is still empty then the file is empty
        if len(delete_list) < 1:
            print('File is empty! Nothing to delete.')
        else:
            with open('Employees.txt', 'r') as employees:
                #assigne read lines to var lines
                lines = employees.readlines()
                #open as write file in order to rewrite without matching ids
                employees_left = open('Employees.txt', 'w')
                for line in lines:
                    #goes line by line from read Employees file before deleting
                    #if no id in the line that is match from the delete list wewrite to file
                    if not any(id in line for id in delete_list):
                        employees_left.write(line)
