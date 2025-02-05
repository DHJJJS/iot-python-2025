# py01_if_statement.py

# if문 : 흐름제어 가장 기본
# 흐름제어문 마지막엔 항상 콜론(:)을 사용해야 함! - 그러지 않으면 문장이 끝나지 않는다.
# if (참이 되는 조건): :(colon), ;(semi-colon)
#   if문 안으로 들어간다!

age = input('나이를 입력하세요.')
age = int(age)

# 만약에 나이가 만 19세가 아니면 담배를 살 수 없음
# 조건이 여러개 일때 and, or로 계속 작성
# if age > 19 or age == 19: # 참인 조건 
if age >= 19:
    print('4,500원입니다.')
else: # False
    print('죽을래? 집에 가!')

grade = input('학점을 입력하십시오(A | B | C | D | F)).').upper() # | 대신 , 써도 상관없음!
# 컴퓨터는 'a'와 'A'는 다르게 처리한다. 따라서, 부가적인 조치 필요 -> upper()

if grade == 'A' or grade == 'B': # 학점이 A거나 B면, 이 구문에 걸리면
    # 구문안으로 들어간다
    print('공부 열심히 하셨네요.')
    print('축하!!')

    if grade == 'A':
        print('장학금을 드리죠!')
    else:
        print('장학금까지 바랬냐??')

elif grade == 'C': # else if를 합친 것. # 학점이 C이면
    print('그럭저럭 하셨네요.')
else:
    print('공부 좀 해라!')

# if는 참 조건 else는 거짓 조건

