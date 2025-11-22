def print_score():
    score = int(input("점수를 입력하세요."))
    if score > 100 or score < 0:
        print("정상적인 점수 범위가 아닙니다.")
    else:
        if score >= 80:
            print("합격입니다.")
        elif score >= 60:
            print("재시험 응시가 필요합니다.")
        else:
            print("불합격입니다.")

    # while True:
    # user_input = input("값을 입력하세요 : ")

    # if user_input.lower() == "z":
    # break


def print_ever():
    input_number = int(input("숫자를 입력하세요."))
    index = 2

    while index < input_number:
        print(index)
        index = index + 2

def print_fibonacci_with_list():
    input_number = int(input("숫자를 입력하세요."))
    print("피보나치 수열 with list")
    list = [1, 1]

    while list[-1] <= input_number:
        print(list[-1])
        list.append(list[-1] + list[-2])

    print("피보나치 수열 without list")

def print_fibonacci_without_list():
    input_number = int(input("숫자를 입력하세요."))
    a = 1
    b = 1
    c = 1

    while c <= input_number:
        print(c)
        c = a + b
        a = b
        b = c
def repeat_function() :
    i = 1

    while i <= 5:
        print_score()
        i = i + 1

# 함수호출 방법
# repeat_function()

arr = ['AA','BB','CC','DD']

for i in arr:
    print(i)

#수학
test = [{ 'answer': [1,3,2,4,5,3,1,2,3,4]},
{ 'answer': [1,1,1,1,1,1,1,1,1,1]},
{ 'answer': [1,5,3,4,5,1,2,3,1,2]},
{'answer': [4,3,2,4,5,3,1,2,3,4]},
{ 'answer': [1,3,2,4,5,3,1,2,3,4]},
{ 'answer': [1,3,2,4,5,3,1,2,3,4]},]

a =  [1,3,2,4,5,3,1,2,3,4]
correct_answer = [2,3,2,4,5,3,1,2,3,4]

#학생 점수 구하기 한 문제당 10점 가정

total_score = 0
for (student, correct) in zip(a, correct_answer):
    print(student, '/', correct)
    if student == correct:
        total_score += 10

print("총점수 :", total_score)




