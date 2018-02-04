class Person:
    corporation = "FC Barcelona 2011"
    def __init__(self, name, age, stress):
        self.name = name
        self.age = age
        self.stress = stress

    def GetStress(self, how_much_stress):
        if how_much_stress > 0:
            self.stress += how_much_stress
        else:
            print("No stress. Happy Life!!!")

    def showInfo(self):
        print("I am {}, {} years old, and I have {}stress".format(self.name, self.age, self.stress))

if __name__ == "__main__":
    p1 = Person("Boss", 40, 30)
    p2 = Person("Employee", 29, 30)

    p1.showInfo()
    p2.showInfo()

    p1.GetStress(50)

    p1.showInfo()
    p2.showInfo()
