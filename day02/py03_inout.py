# py03_inout.py
# 화면입출력

print('출력입니다.')

# 기본 입력
number = input('만 나이를 입력하세요 > ') # 입력방법
# 입력되는 값, 출력되는 값 모두 문자열! 그러므로 연산 (+,-...) 되지 않는다.
number = int(number) # str (문자열) -> int (숫자) 자료형 변경!!!
print(type(number))
print("현재나이는", number + 1) # 여러값을 같이 출력하려면 ,로 구분

# 다중 입력
x, y = input('합산할 두 수를 입력하세요 > ').split() # 공백 기준으로 잘라서 리스트 만들기
x = int(x)
y = int(y)
print(x + y)
