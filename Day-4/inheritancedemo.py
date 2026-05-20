class  employee :
    def __init__(self,name, salary):
        self.name = name
        self.salary = salary

    def high_sal(self, other_emp):
        if self.salary >= other_emp.salary :
            return self
        else :
            return other_emp

class manager(employee)  :
    def __init__(self, name, salary, department):
        super().__init__(name, salary)        #all the parent class constructor to initialize name and sal
        self.department = department

#emp1 = employee("Alice", 50000)
mgr1 = manager("Bob", 85000, "Eng")
#high = emp1.high_sal(mgr1)
#print(f"hign sal is {high.salary}, earned by {high.name}")
print(mgr1.name, mgr1.salary, mgr1.department)