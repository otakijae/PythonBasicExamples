from class_person import Person

class Employee:
    def __init__(self, name, age, stress, work):
        Person.__init__(self, name, age, stress)
        self.work = work

    def DoWork(self, work):
        if work > 0:
            self.work -= work
            self.stress += work*2

    def showInfo(self):
        print("I am {} employee, My name is {}, {} years old".format(Person.corporation,self.name,self.age))
        print("I have {} work to do and, I have {} stress".format(self.work,self.stress))

if __name__ == "__main__":
    p1 = Employee("Pogba", 44, 50, 50)

    p1.showInfo()
