class Employee:
    def __init__(self, FirstName, LastName, IDNumber, HoursWorked, Wage):
        self.FirstName = FirstName
        self.LastName = LastName
        self.IDNumber = IDNumber
        self.HoursWorked = int(HoursWorked)
        self.Wage = float(Wage)

    def WeeklyPay(self):
        if self.HoursWorked > 40:
            overtime = self.HoursWorked - 40
            pay = (overtime * 1.5 * self.Wage) + (40 * 1 * self.Wage)
        else:
            pay = 1 * self.HoursWorked * self.Wage
        return "%.2f" % pay



class HandleFile:

    def read_file(self):
        file1 = open('10.06 Payroll.txt', 'r')
        lines = file1.readlines()
        print("First Name", "Last Name", "ID Number", "Hours Worked", "Hourly Wage", "Weekly Pay")
        for line in lines:
            data = line.split(", ")
            employee = Employee(data[0], data[1], data[2], data[3], data[4])
            print(employee.FirstName,"      ", employee.LastName,"  ", employee.IDNumber, "    " ,employee.HoursWorked,
                  "       ", employee.Wage, "     ", employee.WeeklyPay())


handle_file = HandleFile()
handle_file.read_file()