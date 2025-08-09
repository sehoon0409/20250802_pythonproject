x = 100 #x에 숫자형 100을 대입함
print(x)

x = 100
print(x + 200)

x = "안녕"
y = x +str(3)

print(y)

x = 3 == 5 # 3==5 가 거짓임 으로 boolean 값인 False를 x에 대입함

print(x)

x = "안녕" #x에 문자형 "안녕"을 대입함
print(x)
print(type(x))

x = True   #x에 boolean값 True 대입함
print(x)
print(type(x))

x = [1,2,3,4,5,6,7] #list
print(x)
print(x[0])

x = {'a':1, 'b':3} #dictionary  key:value
print(x)
print(x['a'])
#정오표
example = {
    'python': [True, False, True, True, True, True, True, False, False, True],
    'java': [True, False, False, True, True, True, False, False, False, True],
    'git': [False, False, True, True, False, True, True, True, True, True],
}


print(example)
print(example['python'])
print(example['python'][1])
#문제 답안
python_description = [
    {
        'answer': 1,
        'description': 'python에 대한 설명은 1번이 맞습니다.'
    },
    {
        'answer': "list",
        'description': 'python의 열거형 데이터 타입은 list입니다.'
    },
    {
        'answer': True,
        'description': 'python의 LIST 안에 Dictionary를 사용할 수 있습니다.'
    },
]

print(python_description[0])


list_example = [1, "+", 2, "="]

print(list_example)
print(list_example[0])

#변할수 잇는 데이터는 key값으로 설정 불가
dict_example = {
    1: 'value 1' ,
    # x: 'asdf'      # 변수는 사용 불가능
    # [1,2] : 'asdf' # 리스트 도 사용 불가능
}

print(dict_example)

