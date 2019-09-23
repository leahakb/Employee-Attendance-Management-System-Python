import datetime
class ClockIn():
    def checkExistance(self,id):
        with open('Employees.txt', 'r') as employees:
            lines = employees.readlines()
            EmployeeExists = False
            for line in lines:
                # line.split("\t")[0] is the first element before the tab
                if id in line.split("\t")[0]:
                    # line.split("\t")[1] is the second element before the tab
                    name = line.split("\t")[1]
                    EmployeeExists = True
        if EmployeeExists:
            with open('Attendance log.txt', 'a') as clockInEmployee:
                clockInEmployee.write(id)
                clockInEmployee.write('\t')
                clockInEmployee.write(name)
                clockInEmployee.write('\t')
                clockInEmployee.write(str(datetime.datetime.now()))
                clockInEmployee.write('\n')
        else:
            print('No Employee exists with %s'%id)

class AttendanceReport():
    def report(self,id):
        with open('Employees.txt', 'r') as employees:
            lines = employees.readlines()
            EmployeeExists = False
            for line in lines:
                if id in line.split("\t")[0]:
                    print("Attendance Report for:")
                    print(line)
                    print("ID   Name    ClockIn date and time")
                    print('----------------------------')
                    EmployeeExists = True
        if EmployeeExists:
            with open('Attendance log.txt', 'r') as reportAttendance:
                lines = reportAttendance.readlines()
                for line in lines:
                    if line.split("\t")[0] == id:
                        print(line)
        else:
            print('No Employee exists with %s'%id)

class CurrentMonthReport():
    def report(self):
        currentMonth = str(datetime.date.today())[:7];
        with open('Attendance log.txt', 'r') as readAttendance:
            lines = readAttendance.readlines()
            print("Monthly report for %s" %currentMonth)
            print("ID   Name    ClockIn date and time")
            print("---------------------------")
            for line in lines:
                if line[3:10] == currentMonth:
                    print(line)

class LatenessReport():
    def isLate(self):
        onTime = '09:30'
        with open('Attendance log.txt', 'r') as readAttendance:
            lines = readAttendance.readlines()
            print("Lateness report: ")
            print("ID   Name    ClockIn date and time")
            print("---------------------------")
            for line in lines:
                if line[14:19] > onTime:
                    print(line)

