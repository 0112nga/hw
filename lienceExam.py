def check(answer_list):
    count = 0
    wrong_answer = []
    for x in range(len(answer_list)):
        if answer_list[x] == correctAnswer()[x]:
            count += 1
        else:
            wrong_answer.append(x)
    if count >= 15:
        print('You passed the exam')
    else:
        print('You failed')
    print('Wrong answer: ')
    for x in wrong_answer:
        print(question()[x])
        print('Corect answer is: '+correctAnswer()[x]+'.'+answers()[correctAnswer()[x]][x])
        print('Your answer: '+answer_list[x])


def correctAnswer():
    correct_answer = ['A', 'C', 'A', 'A', 'D', 'B', 'C', 'A', 'C', 'B',
                      'A', 'D', 'C', 'A', 'D', 'C', 'B', 'B', 'D', 'A']
    return correct_answer
def question():
    ques = ['1.When pulling away from the curb, what should you do?',
            '2.A state driving license is valid for use…?',
            '3.If an ambulance or fire service vehicle approaches you from behind with siren on or lights flashing, what must you do?',
            '4.You want to make a U-turn but there is a lot of traffic around. What should you do?',
            '5.A state driving license is valid for use…?',
            '6.You see a blind person holding up their white cane at the roadside. What should you do?',
            '7.What distance should you keep from the vehicle in front when driving at 45 km/h?',
            '8.The number plate of your vehicle must be…?',
            '9.A PUCC (Pollution Under Control Certificate) is valid for how long from the date of issue?',
            '10.If you are involved in a motor accident, how long do you have to report it to the nearest police station?',
            '11.What color are the number plates for private car and motorised two-wheeler owners?',
            '12.It is permissible to exceed the speed limit…?',
            '13.It is acceptable to drink and drive…?',
            '14.You want to make a U-turn but there is a lot of traffic around. What should you do?',
            '15.When pulling away from the curb, what should you do?',
            '16.A circular blue sign with a red border and two red diagonal lines crossing it means what?'
            '17.Traveling at 60 km/h, how far will your vehicle travel in a single second?',
            '18.You are parking your vehicle facing downhill. How should you set your wheels?',
            '19.A cautionary traffic sign is what shape?',
            '20.If you are approaching an unmanned railway crossing, what should you do?']
    return ques
def answers():
    ans = {
        'A' : ['asdv', 'avhjsd', 'ahdvj', 'asdvj', 'asdv', 'ashdv', 'asdvhjsd', 'ahdvbjs', 'ashgdv', 'asdvnsmd',
               'ahsdv', 'advhjsd', 'ajhdvj', 'ahsdvj', 'asdv', 'ashdv', 'asdvhjsd', 'ahdvbjs', 'ashgdv', 'asdvnsmd'],
        'B' : ['bhsdv', 'bdvhjsd', 'bhdvj', 'bhsdvj', 'bsdv', 'bshdv', 'bsdvhjsd', 'bhdvbjs', 'bshgdv', 'bsdvnsmd',
               'bhsdv', 'bdvhjsd', 'bjhdvj', 'bhsdvj', 'bsdv', 'bshdv', 'bsdvhjsd', 'bhdvbjs', 'bshgdv', 'bsdvnsmd'],
        'C' : ['chsdv', 'cdvhjsd', 'cjhdvj', 'chsdvj', 'ccsdv', 'cshdv', 'csdvhjsd', 'chdvbjs', 'cshgdv', 'csdvnsmd',
              'chsdv', 'cdvhjsd', 'cjhdvj', 'chsdvj', 'csdv', 'cshdv', 'csdvhjsd', 'chdvbjs', 'cshgdv', 'csdvnsmd'],
        'D' : ['dhsdv', 'ddvhjsd', 'djhdvj', 'dhsdvj', 'dsdv', 'dshdv', 'dsdvhjsd', 'dhdvbjs', 'dshgdv', 'dsdvnsmd',
               'dhsdv', 'ddvhjsd', 'djhdvj', 'dhsdvj', 'dsdv', 'dshdv', 'dsdvhjsd', 'dhdvbjs', 'dshgdv', 'dsdvnsmd']
    }
    return ans
def test():
    ans = answers()
    ques = question()
    answer_list= []
    for x in range(0,19):
        print(ques[x])
        print('A.'+ans['A'][x]+' B.' +ans['B'][x]+' C.'+ans['C'][x]+' D.'+ans['D'][x])
        print('Input answer:', end=' ')
        student_answer = input()
        answer_list.append(student_answer)
    return answer_list
def main():
    correct_answer = correctAnswer()
    answer_list = test()
    check(answer_list)
main()




