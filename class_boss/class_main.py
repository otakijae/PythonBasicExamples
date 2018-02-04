from class_person import Person
from class_boss import Boss
from class_employee import Employee

p1 = Boss("Pep", 45, 50, 100)
p2 = Employee("Messi", 29, 50, 0)

p1.showInfo()
p2.showInfo()
print("\n")
p1.GiveWork(p2, 100)
print("\n")
p1.showInfo()
p2.showInfo()
print("\n")
p1.GiveWork(p2, 50)
