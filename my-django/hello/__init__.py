from models import Quiz01Calculator, Quiz02Bmi, Quiz03Grade, Quiz05Dice, Quiz07RandomChoice, Quiz08Rps, Quiz09GetPrime, \
    Quiz10LeapYear, Quiz11NumberGolf
from quiz30 import Quiz30
from domains import Member
if __name__ == '__main__':
    while 1:
        menu = input("00계산기 01Bmi 02주사위 03가위바위보 04윤년 05성적표 06멤버선택 07로또 08입출금 09구구단"
                     "10버블 11삽입 12선택 13퀵 14병합 15매직 16지그재그 17직각별 18정삼각별 19예약"
                     "20리스트 21튜플 22딕셔너리 23 24 25 26 27 28 29"
                     "30 31 32 33 34 35 36 37 38 39")
        if menu == 0:
            break
        elif menu == '1':  # 계산기
            q1 = Quiz01Calculator(int(input('첫번째 수')), int(input('두번째 수')), input('+, -, *, /'))
            print('*' * 30 + f'\n {q1.num1} {q1.opcode} {q1.num2} = {q1.calc()}\n' + '*' * 30)

        elif menu == '2':  # BMI
            member = Member()
            q2 = Quiz02Bmi()
            member.name = input('이름 : ')
            member.height = float(input('키 : '))
            member.weight = float(input('몸무게 : '))
            res = q2.bmi(member)
            print('*' * 30 + f'\n이름 : {member.name}, 키 : {member.height}, 몸무게 : {member.weight}, BMI 상태 : {res}\n' + '*' * 30)

        elif menu == '3':  # 성적표
            for i in ['김유신', '강감찬', '유관순', '장원종', '스칼라']:
                print(i)
            q3 = Quiz03Grade((input('이름')), int(input('언어점수')), int(input('영어점수')), int(input('수학점수')))
            print(f'\n#### 성적표 ####\n+ * * 이름: {q3.name}\n'
                  f' * * 언어점수: {q3.kor}\n'
                  f' * * 영어점수: {q3.eng}\n'
                  f' * * 수학점수: {q3.math}\n'
                  f' * * 총점: {q3.total()}\n'
                  f' * * 평균: {q3.avg()}\n'
                  f' * * 합격여부: {q3.grade()} \n')

        elif menu == '5':
            print(Quiz05Dice.cast())

        elif menu == '6':
            q6 = None
        elif menu == '7':
            q7 = Quiz07RandomChoice()
            print(f'당첨 : {q7.chooseMember()}')

        elif menu == '8':
            q8 = Quiz08Rps(int(input('플레이어:')))  # 가위 1 바위 2 보 3
            print(q8.game())
        elif menu == '9':
            q9 = Quiz09GetPrime()
            print(f'')
        elif menu == '10':
            q10 = Quiz10LeapYear(int(input('윤년 평년')))
            print(f'{q10.year}는 {q10.leapyear()}입니다')
        elif menu == '11':
            q11 = Quiz11NumberGolf(int(input('사용자 입력값 : ')))
            print(q11.updown())
        elif menu == '30':
            print(Quiz30.quiz30list())