import json
with open('MBTI_text', 'r') as file:
    mt = json.load(file)


class MBTItest:
    def __init__(self):
        self.answers = []
        self.mbti = []
        self.ei = []
        self.sn = []
        self.tf = []
        self.jp = []

    def test(self):
        print(mt["title"])
        i = 0
        while True:
            print('-'*59)
            print(mt["question"][i])
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
        ei_a = self.ei.count('a')
        ei_b = self.ei.count('b')
        sn_a = self.sn.count('a')
        sn_b = self.sn.count('b')
        tf_a = self.tf.count('a')
        tf_b = self.tf.count('b')
        jp_a = self.jp.count('a')
        jp_b = self.jp.count('b')
        if ei_a > ei_b:
            self.mbti.append('E')
        elif ei_a < ei_b:
            self.mbti.append('I')
        else:
            self.mbti.append('x')
        if sn_a > sn_b:
            self.mbti.append('S')
        elif sn_a < sn_b:
            self.mbti.append('N')
        else:
            self.mbti.append('x')
        if tf_a > tf_b:
            self.mbti.append('T')
        elif tf_a < tf_b:
            self.mbti.append('F')
        else:
            self.mbti.append('x')
        if jp_a > jp_b:
            self.mbti.append('J')
        elif jp_a < jp_b:
            self.mbti.append('P')
        else:
            self.mbti.append('x')
        mbti_result = ''.join(self.mbti)
        print(f'당신의 MBTI는 {mbti_result} 입니다.')


def main():
    mbtitest = MBTItest()
    mbtitest.test()
    mbtitest.calculate()


main()
