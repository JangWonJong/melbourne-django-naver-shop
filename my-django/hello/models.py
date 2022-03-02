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
        if opcode == '+':
            return calc.add()
        elif opcode == '-':
            return calc.sub()
        elif opcode == '*':
            return calc.mul()
        elif opcode == '/':
            return calc.div()

class Bmi(object):
    def __init__(self,name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    def bmi(self):
        bmi = self.weight / (self.height * self.height)*10000

        if bmi >= 35:
            return  f'고도비만'
        elif bmi >= 29.9:
            return  f'중도 비만 (2단계 비만)'
        elif bmi >= 24.9:
            return f'경도 비만 (1단계 비만)'
        elif bmi >= 22.9:
            return f'과체중'
        elif bmi >= 22.9:
            return f'정상'
        else:
            return f'저체중'

class Grade(object):
    def __init__(self,name,kor,eng,math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

    def total(self):
        return self.kor + self.eng + self.math

    def avg(self):
        return self.total()/3
    def getGrade(self):
        pass

    def chkPass(self):# 60점이상이면 합격
        pass

    def grade(self):
        if grade.avg() >= 60:
            return f'합격'
        elif grade.avg() < 60:
            return f'불합격'
        pass


if __name__ == '__main__':

    while 1:
        menu = input('0.Exit 1. 계산기 (+, - ,* ,/) 2.BMI 3.성적표')
        if menu ==0:
            break
        elif menu == '1':
            num1 = int(input('첫번째 수'))
            num2 = int(input('두번째 수'))
            opcode = input('+, -, *, /')
            calc = Calculator(num1, num2)
            print('*'*30 +f'\n {calc.num1} {opcode} {calc.num2}  = {calc.calc()}\n'+'*'*30)

        elif menu == '2':
            name = (input('이름'))
            weight = int(input('몸무게'))
            height = int(input('키'))
            bmi = Bmi(name,height,weight)
            print('*'*30 +f'\n{name} = {bmi.bmi()}입니다\n'+'*'*30)

        elif menu == '3':
            for i in ['국어','영어','수학']:
                print()

            name = (input('이름'))
            kor = int(input('언어점수'))
            eng = int(input('영어점수'))
            math = int(input('수학점수'))
            grade = Grade(kor,eng,math)
            print(f'\n#### 성적표 ####\n+ * * 이름: {name}\n'
                          f' * * 언어점수: {kor}\n'
                          f' * * 영어점수: {eng}\n'
                          f' * * 수학점수: {math}\n'
                          f' * * 총점: {grade.total()}\n'
                          f' * * 평균: {grade.avg()}\n'
                          f' * * 합격여부: {grade.grade()} \n')












