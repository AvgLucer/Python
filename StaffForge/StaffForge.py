#Basic Company Management System
class Basic:
    def __init__(self,name,age,salary,worktime,ids):
        self.name = name
        self.age = age
        self.id = ids
        self.salary = salary
        self.worktime = worktime

class Manager(Basic):
    def __init__(self, name, age, salary, worktime,ids):
        super().__init__(name, age, salary, worktime,ids)
    def pmdetails(self):
        print("~~~~Manager Details~~~~~")
        print(f"Name of the Manager : {self.name}")
        print(f"Age of the Manager {self.age}")
        print(f"Numeric Id of Manager : {self.id}")
        print(f"Salary of the Manager {self.salary}")
        print(f"Worktime of the Manager {self.worktime}")

class Hr(Basic):
    def __init__(self, name, age, salary, worktime, ids):
        super().__init__(name, age, salary, worktime, ids)
    def phrdetails(self):
        print("~~~~HR Details~~~~~")
        print(f"Name of the HR : {self.name}")
        print(f"Age of the HR {self.age}")
        print(f"Numeric Id of HR : {self.id}")
        print(f"Salary of the HR {self.salary}")
        print(f"Worktime of the HR {self.worktime}")


class Employee(Basic):
    def __init__(self, name, age, salary, worktime, ids):
        super().__init__(name, age, salary, worktime, ids)
    def pedetails(self):
        print("~~~~Employee Details~~~~~")
        print(f"Name of the Employee : {self.name}")
        print(f"Age of the Employee {self.age}")
        print(f"Numeric Id of Employee : {self.id}")
        print(f"Salary of the Employee {self.salary}")
        print(f"Worktime of the Employee {self.worktime}")

alldata = []

while True:
    x = int(input("Select Data Entry Type -> 1.Manager Data Entry 2. HR Data Entry 3.Employee Data Entry 4. Print All Data 5. Exit: "))
    if x == 1:
        Managerentry = Manager(input("Enter Name of the Manager:"), int(input("Enter Age of the Manager:")), int(input("Enter Salary of the Manager:")),input("Enter Worktime of Manager:"),int(input("Enter Numeric Id of Manager:")) )
        Managerentry.pmdetails()
        alldata.append(Managerentry)
    elif x == 2:
        HrEntry = Hr(input("Enter Hr name:") , int(input("Enter Age of HR:")),int(input("Enter Salary of Hr:")),input("Enter Worktime of Hr:") , int(input("Enter Numeric Id of Hr:")))
        HrEntry.phrdetails()
        alldata.append(HrEntry)
    elif x == 3:
        EmpEntry = Employee(input("Enter Employee Name:"),int(input("Enter Age of Employee:")), int(input("Enter Salary of Employee:")),input("Enter Worktime of Employee:") , int(input("Enter Id of Employee:")))
        EmpEntry.pedetails()
        alldata.append(EmpEntry)
    elif x == 4:
        print("\n ~~~~ ALL DATA ~~~~~")
        if len(alldata) == 0:
            print("No Data Found")
        else:
            for obj in alldata:
                obj.pmdetails() if isinstance(obj,Manager) else None
                obj.phrdetails() if isinstance(obj,Hr) else None
                obj.pedetails() if isinstance(obj,Employee) else None
    
    elif x  == 5:
        print("Exiting...") 
        break
    else:
        print("Invalid Data Entry Request")    
        