# py02_car.py

# 객체지향 다시
class Car:
    def __init__(self):
        self.__init__('무명', '몰라', '글쎄?')
        print('기본 Car 클래스 생성')
    ## __new__ 사용빈도X, __init__ 많이사용
    ## Car() 호출하면 아래의 메서드가 실행
    ## company, name, plateNumber 모를때는 None.
    def __init__(self, company=None, name=None, plateNumber=None):
        self.__company = company # 멤버변수이름 앞에 __ 쓰면 외부접근 불가
        self.__name = name
        self.__plateNumber = plateNumber
        print('Car 클래스를 새로 생성!')

    # 클래스 자체가 출력되는데, __sts__ 문자열로 출력되도록 바꿔줌
    def __str__(self):
        return f'제차는 {self.__name}이고, 차번호는 {self.__plateNumber} 입니다.'
    
    # 외부에서 잘못된 차번호를 넣으면 안 들어감
    def setPlateNumber(self,NewPlatenumber):
        if type(NewPlatenumber) is 'str':
            self.__plateNumber = NewPlatenumber

    def setName(self, newName='글쎄요'): # 이름을 모를 때 글쎄요로 대체
        self.__name = newName

    def getName(self):
        return self.__name
    
    # setName - getName은 항상 같이 간다.


# 모듈화 하려면 예제소스가 없어야 함
# myCar = Car('현대차', '아이오닉', '54라9537')
# 파라미터명 = 값으로 매개변수 순서를 변경가능
# myCar = Car(name='아이오닉', plateNumber='54라9537', company='현대차')

# print(myCar) # 차의 번호를 출력하고 싶음
# myCar.__plateNumber = 2018 # 클래스 외부에서 잘못된 데이터를 넣어도 문제가 발생X # 객체지향에서 중요한 개념
# print(myCar)
# myCar.setPlateNumber('2025')
# print(myCar)

# # 숫자는 들어가지 않고 ''로 문자처리하면 들어감

# yourCar = Car()
# print(yourCar)
# yourCar.setPlateNumber('285구8899')
# print(yourCar)
# yourCar.setName()
# print(yourCar)