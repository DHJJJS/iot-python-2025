# py05_operator.py
# 연산자

# 사칙연산 : + - * /
a, b = 15, 14
# Shift + Del 는 한줄 삭제 (매우 효율!)
print(a + b)
print(a - b)
print(a * b)

# 나누기 연산자 /, //, % (세개나 필요함)
a = 14
b = 4
print(a / b) # 나눈 결과는 float
print(a // b) # 나눈 몫, int
print (a % b) # 나머지, int

# 거듭제곱(Power) **
print(2 ** 10) ## 2의 5제곱 = 32비트 / 2의 6제곱 = 64비트. / 2의 10제곱 = 해상도 1024

# 연산자 우선순위 (어렵다)
## 계산식이 복잡해서 연산자 우선순위를 잘 모르겠으면 () 사용
print((3 + 4) * 7) 
print(3 + (4 * 7)) 


## 리스트 연산
## last index = len(list) - 1
listSample = [1, 3, 5, 7, 9]
print(listSample[0])
print(len(listSample)) # 리스트의 길이

print(listSample[1])
print(listSample[2])
print(listSample[3])
print(listSample[4])

listSample[4] = 11

print(listSample[len(listSample) - 1])
# 파이썬에서는 마지막 요소를 가져올 때 print(listSample[-1])하면 간단하다.
# print(listSample[5])

## 문자열 연산 : +, * 만 존재
# 연산은 숫자만 되는 게 아니다!
greeting = 'Hello'
target = 'World'
print(greeting, target) # 공백 띄워줌 # 문자열 연산 X
print(greeting + ' ' + target) # 공백이 사이에 없음 # 문자열 연산 + string concatenate
print('{0} {1}'.format(greeting, target))
print(f'{greeting} {target}')

print(greeting * 5) # 해당 문자열을 * 수로 반복
# 문자열 연산은 +, * 밖에 없다.

## 문자열(Charactor Array) : List와 유사하지만 값 수정 불가
print(greeting[1]) # 리스트 연산
# greeting[0] = 'C'
print(greeting) 

## 리스트연산, 슬라이싱
listSample = ['2', '0', '2', '5', '-', '0', '2', '-', '0', '4']
current = '2025-02-04'

for i in listSample:
    print(i, end='')
print()

print(current)
# 준비 끝

# 인덱싱, 인덱스에 있는 값을 가져오기
print(listSample[-7])
print(current[-7])

# -N = 인덱싱을 거꾸로 읽어주는 것. 이건 파이썬에서만 있다.

# 슬라이싱, 리스트를 자르기
## [start:end] : end - 1까지만 추출 <- 이게 파이썬의 상당히 특징적인 부분이다.
print(listSample[0:3 + 1])
print(current[0:3 + 1])

# 2025-02-04
year = current[0:3 + 1]
month = current[5:6 + 1]
day = current[8:] # end 끝까지는 숫자 생략
print(year, month, day)
print(current[-2:])

## 문자열 연산 중 함수를 사용
full_name = "Hugo MG. Sung"

# 자르기
print(full_name.split())
print(full_name.split(' '))


names = full_name.split(' ')
print(type(names))
print(names)

names = full_name.split('.')
print(type(names))
print(names)

# 바꾸기
print(full_name.replace('Hugo Mg.', 'Ashley'))

# 공백제거
origin = '     Hello  ~     '
print(f'//{origin}//')
print(f'//{origin.lstrip()}//')
print(f'//{origin.rstrip()}//')
print(f'//{origin.strip()}//')

# 단어찾기
full_name = "Hugo MG. Sung"
print(full_name.find('G'))
print(full_name.find('g'))
print(full_name.find('h')) # -1 : h를 찾을 수 없음 !

print(full_name.count('g')) # g가 문장에 몇번 존재
# print(full_name.index('h')) # 오류발생!

print(full_name.upper())
print(full_name.lower())

## T로 자를때
# '', "" == Empty(비어있다.)
# ' ', " " == Space(공백존재)
origin = 'TESTSTRING'
print(origin.split('T'))