# py05_funciton.py
# 함수, Function, Methodc, Procedure...
# 인자, 파라미터, 매개변수, Parameter, Argument...
# def 함수명(인자1, 파라미터2, 매개변수3):
#       함수안으로 진입


def say_hi():
    print('안녕~ ')
    return

# name = '명건'
def say_hello(name):
    print(f'{name}야, 안녕!!')
    return

def get_age(birthYear):
    age = 2025 - birthYear
    return age

def closing():
    return '바이바이~'

print('인사하기:', end=' ')
say_hi() # 함수 호출
say_hi()

name = input('이름입력 > ')
print('이름으로 인사하기:', end=' ')
say_hello(name)

#위 아래 name은 이름은 같아도 전혀 다르다. 지역 변수와 전역 변수.

year = int(input('생일년도 >'))
real_age = get_age(year)
print(f'나이는:{real_age}세')