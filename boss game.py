print("게임에 오신 것을 환영합니다!")

import random
weapon_level = 0
boss_level = 0
is_dragon_slayer = False
def show_status(is_dragon_slayer):
    title = "[드래곤 처치자]" if is_dragon_slayer else "없음"
    print(f"칭호: {title}")
    print(f"현재 무기 레벨: {weapon_level}")
    print(f"현재 보스 레벨: {boss_level}")
#up : 강화 성공! 레벨이 +1 됩니다.
#keep : 변화 없음. 현재 레벨을 유지합니다
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

    if is_dragon_slayer : print("[드래곤 처치자] 전설의 용사님, 환영합니다!")

    show_status(is_dragon_slayer)

    print("1. 무기 강화")
    print("2. 보스 도전")
    print("0. 종료하기")
    choice = input("숫자를 입력하세요 (0을 입력하면 종료):")

    if choice == "0":
        print("게임을 종료합니다")
        break


    elif choice == "1" :
        ran_num = random.randrange(0,99)
        rate = upgrade_rates[weapon_level]

        if ran_num < rate["up"]:
            result = "up"
        elif ran_num < rate["up"] + rate["keep"]:
            result = "keep"
        elif ran_num < rate["up"] + rate["keep"] + rate["down"]:
            result = "down"
        else:
            result = "break"


        if result == "up":
            if weapon_level < 10:
                weapon_level += 1
            else: print("더 이상 업그레이드가 불가합니다")
        if result == "down":
            if weapon_level < 10:
                weapon_level -= 1
            else: print("더 이상 레벨이 떨어질수 없습니다")
        if result == "break":
            if weapon_level < 10:
                weapon_level = 0
        print(f"강화 시도 결과: [{result}]")

    elif choice == "2":
        boss_names = ['거짓 종막의 연출가',
                     '철혈의 패왕',
                     '부유한 밤의 아버지',
                     '구원의 마왕',
                     '묵시록의 최후룡',
                     '악마같은 불의 심판자',
                     '심연의 흑염룡',
                     '긴고아의 죄수',
                     '형용할 수 없는 아득함',
                     '은밀한 모략가' ,
                     '가장 오래된 꿈']

        print("현재 보스:", boss_names[boss_level])

        level_diff = weapon_level - boss_level

        if level_diff <= -3:
            win_rate = 0
        elif level_diff == -2:
            win_rate = 20
        elif level_diff == -1:
            win_rate = 30
        elif level_diff == 0:
            win_rate = 50
        elif level_diff == 1:
            win_rate = 70
        elif level_diff == 2:
            win_rate = 90
        elif level_diff >= 3:
            win_rate = 100
        ran_num = (random.randint(0, 99))


        if ran_num < win_rate :
            if boss_level < 11:
                boss_level += 1
                print("보스 처치 성공!")
        elif ran_num >= win_rate :
            if boss_level < 11:
               print("처참하게 패배했습니다...")
               boss_level +=0

        is_dragon_slayer = False

        if boss_level==11:
            print('축하합니다! 모든 보스를 제압했습니다!')
            is_dragon_slayer = True


















