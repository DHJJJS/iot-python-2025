# 변수와 자료형
# 변수는 => 변하는 수(Variable) <-> 상수(Constant)
# 상수 예 Pi = 3.14159265727.....

# 변수
a = None # 특수형 -> 아무것도 아니라고 지정해주는 값. 중요하다. # Noen타입 <- 이런 용어 잘 기억해두기
print(a) # a라는 변수에 무슨 값이 들어있는지 콘솔에 출력해줘
print(type(a)) # a에 있는 값을 꺼내서, 그 타입이 뭔지 출력해줘

a = 10 # 10과 10.0은 출력은 같더라도 다른 값이다. 정수(소수점없는 수), Integer <- 줄여서 Int라고 부름
print(a) # 함수는 늘 괄호를 같이 사용
print(type(a))

a = 12.34 # 실수(소수점아래 수수), Float
print(a)
print(type(a))

a = 0b11111110 # 0과 1로 수를 표현하는 방식(2진수), Binary
print(a)
print(type(a))

a = 0xFE # 16진수(0~9,A,B,C,D,E,F[15]로 수를 표현방식), Hex
print(a)
print(type(a))

a = 1_900_000_000 # 언더바는 사라지고 숫자만 출력됨. 천단위마다 쉼표와 같이 표현(Tip)
print(a)
print(type(a))

a = "Life is short, You need Python" # 문자열, String
print(a)
print(type(a))

a = 'Life is short, You need Python' # 문자열 # '든' "든" 출력시에 아무 차이가 없다.
print(a)
print(type(a))

a = (3 > 1) # 불형 True | False, Boolean 
print(a)
print(type(a))