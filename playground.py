import random
import time


# def print_times_table(number):
#     print(number, "*", 1, "=", number*1)
#     print(number, "*", 2, "=", number*2)
#     print(number, "*", 3, "=", number*3)
#     print(number, "*", 4, "=", number*4)
#     print(number, "*", 5, "=", number*5)
#     print(number, "*", 6, "=", number*6)
#     print(number, "*", 7, "=", number*7)
#     print(number, "*", 8, "=", number*8)
#     print(number, "*", 9, "=", number*9)
#
# def examlpe_function(input_arg: int) -> int:
#     print("숫자 형태를 입력받아서 다른 숫자형태를 반환")
#     return input_arg + 5
#
# def updown():
#     result = random.randrange(1,10)
#
# while True:
#     user_input = input("값을 입력하세요 : ")
#
#     if user_input.lower() == "z":
#         break

    #test
def updown():
# random.randrange ( n, m )   n <= result < m
    print("WELCOME TO UP DOWN")
    result = random.randrange(1, 100)

    while True:
        x = int(input("숫자를 입력하세요:"))

        if x > result:
            print("Down")

        if x < result:
            print("Up")

        if x == result:
            print("정답입니다.")
            break


def quiz():
    print("WELCOME TO QUIZ!")

    word = { "apple" : "사과" ,
               "banana" : "바나나" ,
               "grape" : "포도" ,
               "melon" : "멜론"}

    score = 0
    test_list = list(word.keys())

    for i in range(10) :
        test = random.randrange(test_list)
        answer = word[test]







def stop_watch():
    print("WELCOME TO UP STOPWATCH")
    # random 초를 제공하면 ex) 7초
    start = time.time()

    input("c를 입력하시오:")

    end = user_input(time.time() - start)

    if 6.7 <= end - start <= 7.3:
        print("성공입니다!")
    else : print("다시 시도해 보세요")



while True:
    print('''
    ================메뉴================
    A. Up & Down 게임
    B. 영어 낱말 맞추기
    C. Stop watch 게임
    Z. 프로그램 종료
    ====================================
    ''')
    user_input = input("값을 입력하세요 : ")

    if user_input.lower() == "a":
        updown()

    elif user_input.lower() == "b":
        quiz()
    elif user_input.lower() == "c":
        stop_watch()
    elif user_input.lower() == "z":
        break


