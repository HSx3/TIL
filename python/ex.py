# 도형만들기
# 파이썬 클래스를 활용하여 꼭지점과 원을 표현하시오.
# point 클래스에 대한 명세는 다음과 같습니다.
# 인스턴스가 생성될 때, 정수 두 개를(좌표 값) 인자로 받아 생성됩니다. 
# 각각 인스턴스 변수명은 x, y 입니다.


class Point:
    def __init__(self, x=0, y=0):
        self.x = int(x)
        self.y = int(y)


class Circle:
    def __init__(self, center, r):
        self.center = center
        self.r = r

    def get_area(self):
        return self.r ** 2 * 3.14

    def get_perimeter(self):
        return 2 * 3.14 * self.r

    def get_center(self):
        return self.center.x, self.center.y

    def print(self):
        print(f'Circle: ({self.center.x}, {self.center.y}), r: {self.r}')


p1 = Point(0, 0)
c1 = Circle(p1, 3)
print(c1.get_area())
print(c1.get_perimeter())
print(c1.get_center())
c1.print()