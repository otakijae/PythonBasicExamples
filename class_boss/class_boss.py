from class_person import Person

class Boss:
    def __init__(self, name, age, stress, work):
        Person.__init__(self, name, age, stress)
        self.work = work

    def GiveWork(self, other, work):
        if work > 0 and self.stress > 0:
            self.work -= work
            self.stress -= work*2

            other.work =+ work
            other.stress =+ work*2
        else:
            print("No stress! No work! Leave the office!")

    def showInfo(self):
        print("I am {} boss, My name is {}, {} years old".format(Person.corporation,self.name,self.age))
        print("I have {} work to do and, I have {} stress".format(self.work,self.stress))

if __name__ == "__main__":
    p1 = Boss("Jae", 23, 50,50)

    p1.showInfo()
