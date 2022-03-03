import random




class Quiz01Calculator(object):

    def __init__(self, num1, num2, opcode):
        self.num1 = num1
        self.num2 = num2
        self.opcode = opcode

    def calc(self):
        if self.opcode == '+':
            return self.num1 + self.num2
        elif self.opcode == '-':
            return self.num1 - self.num2
        elif self.opcode == '*':
            return self.num1 * self.num2
        elif self.opcode == '/':
            return self.num1 / self.num2


class Quiz02Bmi(object):


    @staticmethod
    def bmi(member):
        this = member
        bmi = this.weight / (this.height * this.height)*10000

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

def myRandom(start, end):
    return random.randint(start, end)

class Quiz05Dice(object):
    @staticmethod
    def cast():
        return myRandom(1,6)


class Quiz07RandomChoice(object):
    def __init__(self): # 803호에서 랜덤으로 1명 이름 추출
        self.members = ['홍정명', '노홍주', '전종현', '정경준', '양정오',
                        "권혜민", "서성민", "조현국", "김한슬", "김진영",
                        '심민혜', '권솔이', '김지혜', '하진희', '최은아',
                        '최민서', '한성수', '김윤섭', '김승현',
                        "강 민", "최건일", "유재혁", "김아름", "장원종"]
    def chooseMember(self):
        ran = myRandom(0,23)
        return self.members[ran]

class Quiz08Rps(object):
    def __init__(self, user):
        self.user = user
        self.com = myRandom(1,3)

    def game(self):
        c = self.com
        u = self.user
        # 1 가위 2 바위 3 보
        rps = ['가위', '바위', '보']
        if u == 1:
            if c == 1:
                res = f'플레이어: {rps[0]} 컴퓨터: {rps[0]}, 결과 무승부'
            elif c == 2:
                res = f'플레이어: {rps[0]} 컴퓨터: {rps[1]}, 결과 패배'
            elif c == 3:
                res = f'플레이어: {rps[0]} 컴퓨터: {rps[2]}, 결과 승리'
        if u == 2:
            if c == 1:
                res = f'플레이어: {rps[1]} 컴퓨터: {rps[0]}, 결과 승리'
            elif c == 2:
                res = f'플레이어: {rps[1]} 컴퓨터: {rps[1]}, 결과 무승부'
            elif c == 3:
                res = f'플레이어: {rps[1]} 컴퓨터: {rps[2]}, 결과 패배'
        if u == 3:
            if c == 1:
                res = f'플레이어: {rps[2]} 컴퓨터: {rps[0]}, 결과 패배'
            elif c == 2:
                res = f'플레이어: {rps[2]} 컴퓨터: {rps[1]}, 결과 승리'
            elif c == 3:
                res = f'플레이어: {rps[2]} 컴퓨터: {rps[2]}, 결과 무승부'

        return res




class Quiz09GetPrime(object):
    def __init__(self):
        pass

class Quiz10LeapYear(object):
    def __init__(self):
        pass

class Quiz11NumberGolf(object):
    def __init__(self):
        pass

class Quiz12Lotto(object):
    def __init__(self):
        pass

class Quiz13Bank(object): # 이름, 입금, 출금만 구현
    def __init__(self):
        pass

class Quiz14Gugudan(object): # 책받침구구단
    def __init__(self):
        pass















