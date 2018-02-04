class Calculator:
    def __init__(self, exp):
        self.orgExp = exp.replace(" ", "") 
        #self.postfixExp = exp

    def GetWeight(self, oprt):
        if oprt == '*' or oprt == '/':
            return 9
        elif oprt =='+' or oprt =='-':
            return 7
        elif oprt == '(':
            return 5
        else:
            return -1

    
    def ConvertToPostfix(self):
        listExp = []
        listStack = []

        for ch in self.orgExp:
            if ch.isdigit():
                listExp.append(ch)
            else:
                if self.GetWeight(ch) == 5 or not listStack:
                    listStack.append(ch)
                elif ch == ')':
                    while 1:
                        op = listStack.pop()
                        if op == '(':
                            break
                        listExp.append(op)
                        
                elif self.GetWeight(ch) > self.GetWeight(listStack[-1]):
                    listStack.append(ch)
                elif self.GetWeight(ch) == self.GetWeight(listStack[-1]):
                    listExp.append(listStack.pop())
                    listStack.append(ch)
                elif self.GetWeight(ch) < self.GetWeight(listStack[-1]):
                    listExp.append(listStack.pop())
                    listStack.append(ch)

        if listStack:
            while listStack:
                listExp.append(listStack.pop())

        self.postfixExp = "".join(listExp)
        return self.postfixExp

    
    def calcTwoOp(self, op1, op2, oprt):
        if oprt == "+":
            return op1 + op2
        elif oprt == "-":
            return op1 - op2
        elif oprt == "*":
            return op1 * op2
        elif oprt == "/":
            return op1 // op2
    
    def Calculate(self):
        #list for stack
        stackOperand = []
        for ch in self.postfixExp:
            #If it is a number under 10, prepare calculation
            if ch.isdigit():
                stackOperand.append(int(ch))
            #If it is an operand which is not number, do calculate
            else:
                op2 = stackOperand.pop()
                op1 = stackOperand.pop()
                result = self.calcTwoOp(op1, op2, ch)
                stackOperand.append(result)
        return result

if __name__ == "__main__":
    calc = Calculator(input("Input : "))
    print(calc.ConvertToPostfix())
    result = calc.Calculate()
    print(result)
