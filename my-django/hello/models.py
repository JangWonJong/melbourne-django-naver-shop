class Calculator(object):

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def sub(self):
        return self.num1 - self.num2

    def mul(self):
        return self.num1 * self.num2

    def div(self):
        return self.num1 / self.num2

    def calc(self):
        pass


if __name__ == '__main__':

    while 1:
        menu = input('0.Exit 1. 계산기 (+, - ,* ,/)')
        if menu ==0:
            break
        elif menu == '1':
            num1 = int(input('첫번째 수'))
            num2 = int(input('두번째 수'))
            opcode = input('+, -, *, /')
            calc = Calculator(num1, num2)

            if opcode == '+':
                result = calc.add()
            elif opcode == '-':
                result = calc.sub()
            elif opcode == '*':
                result = calc.mul()
            elif opcode == '/':
                result = calc.div()

            print('*'*30 +f'\n {calc.num1} {opcode} {calc.num2}  = {result}\n'+'*'*30)



