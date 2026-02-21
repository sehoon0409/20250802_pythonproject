# STEP.0
print("게임에 오신 것을 환영합니다!")

#무기 레벨 변수 만들기 ⚔️
weapon_level = 0
#up : 강화 성공! 레벨이 +1 됩니다.
# keep : 변화 없음. 현재 레벨을 유지합니다
#down : 강화 실패. 레벨이 -1 됩니다.
#break : 최악의 결과! 무기가 파괴되어 레벨 0이 됩니다.

#레벨별 강화 확률표 (데이터 설계) 📊
upgrade_rates = [ { "up": 70, "keep": 30, "down": 0, "break": 0,},
                  { "up": 60, "keep": 25, "down": 10, "break": 5},
                  { "up": 50, "keep": 30, "down": 15, "break": 5},
                  { "up": 45, "keep": 30, "down": 20, "break": 5},
                  { "up": 40, "keep": 30, "down": 20, "break": 10},
                  { "up": 35, "keep": 30, "down": 25, "break": 10},
                  { "up": 30, "keep": 30, "down": 30, "break": 10},
                  { "up": 25, "keep": 30, "down": 30, "break": 15},
                  { "up": 20, "keep": 30, "down": 30, "break": 20},
                  { "up": 15, "keep": 30, "down": 30, "break": 25},
                  { "up": 0, "keep": 100, "down": 0, "break": 0}]

#무한 반복 구조 만들기 (반복문)
while True :
    print("1. 무기 강화")
    print("0. 종료하기")
    choice = input("숫자를 입력하세요 (0을 입력하면 종료):")

    if choice == "0":
        print("게임을 종료합니다")
        break


    if choice == "1" :
       print("hello world")
       break




