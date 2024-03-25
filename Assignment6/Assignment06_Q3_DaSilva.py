class Employee:
    def __init__(self, name, position, base_salary) -> None:
        self.name = name
        self.position = position
        self.base_salary = base_salary
    
    def calculate_salary(self):
        return self.base_salary
    
class HourlyEmployee(Employee):
    def __init__(self, name, position, base_salary, hours_worked, hourly_rate) -> None:
        super().__init__(name, position, base_salary)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate
    
    def calculate_salary(self):
        return super().calculate_salary() + self.hours_worked * self.hourly_rate

class CommissionEmployee(Employee):
    def __init__(self, name, position, base_salary, sales, sales_percentage) -> None:
        super().__init__(name, position, base_salary)
        self.sales = sales
        self.sales_percentage = sales_percentage
    
    def calculate_salary(self):
        return super().calculate_salary() + self.sales + self.sales_percentage
    
def main():

    employee = Employee("caio", "manager", 100000)
    hourly_employee = HourlyEmployee("caio", "manager", 100000, 100, 0.5)
    commission_employee = CommissionEmployee("caio", "manager", 100000, 200, 0.2)

    employee_list = [employee, hourly_employee, commission_employee]

    for employee in employee_list:
        print(employee.calculate_salary())

main()