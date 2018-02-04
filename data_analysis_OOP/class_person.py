class Person:
    #class variable
    planet = "Earth"
    
    def __init__(self,name, age, money):
        self.name = name
        self.age = age
        self.money = money

    def giveMoney(self, other, how_much):
        if how_much <= self.money:
            self.money -= how_much
            other.money += how_much
        else:
            print("You don't have {}".format(how_much))

    @staticmethod
    def SavingCalculator(amount_per_month, months):
        return amount_per_month * months

    def showInfo(self):
        print("I am {}, I have {}won".format(self.name, self.money))

if __name__ == "__main__":      #similar to // int main()
    p1 = Person("sanchez", 35, 5000)
    p2 = Person("jaehyuk", 23, 2000)

    p1.giveMoney(p2, 3000)

    p1.showInfo()
    p2.showInfo()
