class Quiz30:
    def __init__(self):
       pass
    @staticmethod
    def quiz30list():
            list1 = [1,2,3,4]
            #print(list1,type(list1))
            list2 = ['math', 'english']
            print('리스트1: ',list1[0], list1[-1], list1[-2])
            print('리스트1에서 1번째,2번째 성분출력: ', list1[1:3])
            print('리스트2에서 math출력:', list2[0])
            print('리스트2에서 a출력: ', list2[0][1])
            print('리스트2에서 math english 출력 :', list2[0],list2[1])
            list3 = [1, '2', [1, 2, 3]]
            list4 = [1,2,3]
            list5 = [4,5]
            list4[-2:] = []
            print('리스트4 두배 출력: ', 2*list4)
            print('리스트4와 리스트5 합치기:', list4+list5)
            print('리스트4에 리스트5 성분합치기:', list4.append(list5))
            print('리스트4,5에서 [1,2] 출력해보기', list4)
            list6 = [[1,2],[0,5]]
            # 2를 출력해보시오
            a = [1,2]
            b = [0,5]
            c = [a,b]
            c[0][1] = 10
            print(list6[0][1])
            print(c)

            #range = range(10)










    def quiz31tuple(self):
        tuple1 = (1,2)
        tuple2 = (0,(1,4))
        print(tuple1+tuple2)



    def quiz32(self):
        pass
