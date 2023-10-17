import json
with open('MBTI_text.json', 'r') as file:
    mt = json.load(file)


class MBTItest:
    def __init__(self):
        self.answers = []
        self.mbti = []
        self.ei = ['E', 'I']
        self.sn = ['S', 'N']
        self.tf = ['T', 'F']
        self.jp = ['J', 'P']
        self.ca = 0
        self.cb = 0

    def test(self):
        print(mt["title"])
        i = 0
        while True:
            print('-'*59)
            print(f'{i+1}번 문제 : {mt["question"][i]}')
            print(mt["tip"])
            answer = input('입력 (a/b) : ')
            i += 1
            if answer == 'a':
                self.answers.append('a')
            elif answer == 'b':
                self.answers.append('b')
            elif answer == 'back':
                if i >= 2:
                    i -= 2
                    del self.answers[-1]
                elif i < 2:
                    print(mt["no_question"])
                    i -= 1
            elif answer == 'quit':
                i = 70
                print(mt["end_program"])
            else:
                print(mt["error_answer"])
                i -= 1
            if i == 70:
                break

    def count_ab(self):
        lists = [self.ei, self.sn, self.tf, self.jp]
        for i in range(len(lists)):
            self.ca = lists[i].count('a')
            self.cb = lists[i].count('b')
            if self.ca > self.cb:
                self.mbti.append(lists[i][0])
            elif self.ca < self.cb:
                self.mbti.append(lists[i][1])
            else:
                self.mbti.append('x')

    def calculate(self):
        for i in range(len(self.answers)):
            if i % 7 == 0:
                self.ei.append(self.answers[i])
            elif i % 7 == 1 or i % 7 == 2:
                self.sn.append(self.answers[i])
            elif i % 7 == 3 or i % 7 == 4:
                self.tf.append(self.answers[i])
            elif i % 7 == 5 or i % 7 == 6:
                self.jp.append(self.answers[i])
        MBTItest.count_ab(self)

        mbti_result = ''.join(self.mbti)
        print(f'당신의 MBTI는 {mbti_result} 입니다.')


def main():
    mbtitest = MBTItest()
    mbtitest.test()
    # mbtitest.count_ab()
    mbtitest.calculate()


main()
