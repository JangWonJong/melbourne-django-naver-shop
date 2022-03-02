
def main():
    while 1:
        menu = input('0.Exit 1. 계산기 (+, - ,* ,/) 2.BMI 3.성적표')
        if menu == 0:
            break
        elif menu == '1':  # 계산기
            q1 = Quiz01Calculator(int(input('첫번째 수')), int(input('두번째 수')), input('+, -, *, /'))
            print('*' * 30 + f'\n {q1.num1} {q1.opcode} {q1.num2} = {q1.calc()}\n' + '*' * 30)

        elif menu == '2':  # BMI
            q2 = Quiz02Bmi((input('이름')), int(input('몸무게')), int(input('키')))
            print('*' * 30 + f'\n이름 : {q2.name}, 키 : {q2.height}, 몸무게 : {q2.weight}, BMI 상태 : {q2.bmi()}\n' + '*' * 30)

        elif menu == '3':  # 성적표
            for i in ['김유신', '강감찬', '유관순', '장원종', '스칼라']:
                print()
            q3 = Quiz03Grade((input('이름')), int(input('언어점수')), int(input('영어점수')), int(input('수학점수')))
            print(f'\n#### 성적표 ####\n+ * * 이름: {q3.name}\n'
                  f' * * 언어점수: {q3.kor}\n'
                  f' * * 영어점수: {q3.eng}\n'
                  f' * * 수학점수: {q3.math}\n'
                  f' * * 총점: {q3.total()}\n'
                  f' * * 평균: {q3.avg()}\n'
                  f' * * 합격여부: {q3.grade()} \n')

        elif menu == '5':
            q5 = Quiz05Dice()

        elif menu == '6':
            q6 = Quiz06RandomGenerator()

        elif menu == '7':
            q7 = Quiz07RandomChoice()



class Quiz01Calculator(object):

    def __init__(self, num1, num2, opcode):
        self.num1 = num1
        self.num2 = num2
        self.opcode = opcode

    def add(self):
        return self.num1 + self.num2
    def sub(self):
        return self.num1 - self.num2
    def mul(self):
        return self.num1 * self.num2
    def div(self):
        return self.num1 / self.num2

    def calc(self):
        if self.opcode == '+':
            return self.add()
        elif self.opcode == '-':
            return self.sub()
        elif self.opcode == '*':
            return self.mul()
        elif self.opcode == '/':
            return self.div()

class Quiz02Bmi(object):
    def __init__(self, name, height, weight):
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

class Quiz03Grade(object):
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

    def grade(self):
        if self.avg() >= 60:
            return f'합격'
        elif self.avg() < 60:
            return f'불합격'
        pass

class Quiz04GradeAuto(object):
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

class Quiz05Dice(object):
    def __init__(self):
        pass

class Quiz06RandomGenerator(object):
    def __init__(self): # 원하는 범위의 정수에서 랜덤값 1개 추출

        pass
class Quiz07RandomChoice(object):
    def __init__(self): # 803호에서 랜덤으로 1명 이름 추출
        self.members = ['홍정명', '노홍주', '전종현', '정경준', '양정오',
                        "권혜민", "서성민", "조현국", "김한슬", "김진영",
                        '심민혜' , '권솔이', '김지혜' , '하진희' , '최은아',
                        '최민서', '한성수', '김윤섭', '김승현',
                        "강 민", "최건일", "유재혁", "김아름", "장원종" ]



if __name__ == '__main__':
    main()












