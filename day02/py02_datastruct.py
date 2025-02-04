# py02_datastruct.py
# 복합자료형
# 자료구조 및 알고리즘

# 리스트 사용 이전
a = 1
b = 2
c = 3
d = 4
e = 5

sum = a + b + c + d + e
print(sum)

# 리스트(배열) 사용 - 다른 언어에선 리스트와 배열은 다른 것. [] <- 를 쓴다
f = [1,2,3,4,5]
print(f)
print(type(f))

f = ['Life', 'is', True, 0, None, [1,2,3]] # 리스트 안에 또 리스트를 넣을 수 있다.
print(f)
print(f[0]) # 첫번째 값은 Life다. 그리고 컴퓨터는 모든 처음 값이 '0'이다.
# 리스트의 한 요소에도 값을 집어넣을 수 있음
f[3] = 100
print(f)

## 튜플 () <- 를 쓴다
# 리스트와 거의 흡사하지만 가장 큰 특징은 값을 변경할 수 없다는 것이다.
t = (1,2,3,4)
print(t)
print(t[3])
# t[0] = 5 # 주석 토글 Ctrl + / 사용
print(type(t))

## 딕셔너리 (사전 타입) {key : value} 의 집합 {} <- 를 쓴다
spiderman = { 'name': 'Peter Parker', 'age': 20, 'weapon': 'Web Shooter'}
print(spiderman)
print(type(spiderman))

print(spiderman['name'])
spiderman['age'] = 21 # 튜플 말고는 모두 값을 변경할 수 있다. 
print(spiderman) 

## 집합 (), [], {} 다 사용, {} <- 원래 집합기호, set() <- 튜플 변환 set[] <- 리스트 변환,
# 수학의 집합과 동일, 중복 제거. 리스트처럼 인덱스가 없음
s = set([1, 3, 5, 7, 9, 5])
print(s)
print(type(s))

s = set('Hello World') # 공백도 값이다. 순서가 없고 그때 그때 바뀐다.
print(s)

## 변수명 지정 방식
## 의미있는 단어들의 조합으로 만들 것
## 길이는 상관없다.
phoneNumber = '010-6688-7733'
salaryBankAccount = '866-12-335566'

samsung = ''
samsung1 = ''
# 1samsung = '' # 숫자로 변수명을 취할 수 없다.
_samsung = '' 
samsung_ = ''
# samsung* = '' # _ 이외의 특수문자는 사용불가 
# samsung! = ''
# samsung-apple = '' # 파이썬 연산자는 사용불가