import datetime

from people.people import get_employees
from salary.salary import calculate_salary

date_time = datetime.datetime.today()

if __name__ == '__main__':
    calculate_salary(1000, 3000)
    get_employees(1)
    print(date_time)