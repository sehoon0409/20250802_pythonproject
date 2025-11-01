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
    #user_input = input("값을 입력하세요 : ")

    #if user_input.lower() == "z":
        #break

input_number = int(input("숫자를 입력하세요."))
index = 2

print("짝수 출력 ----->")
while index <= input_number:
        print(index)
        index = index + 2

print("피보나치 수열 with list")
list=[1,1]

while list[-1] <= input_number :
    print(list[-1])
    list.append(list[-1] + list[-2])


print("피보나치 수열 without list")

a = 1
b = 1
c = 1

while c <= input_number:
    print(c)
    c = a + b
    a = b
    b = c







