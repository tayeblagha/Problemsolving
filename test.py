from collections.abc import Iterable


class Point:
    def __init__(self,x):
        self.x=x
    #x: float= 0.0
    y: float=0.0
    def __repr__(self) -> str:
        return f"({self.x},{self.y})"

p0=  Point(12.2)

print(p0)

