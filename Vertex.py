import random

class Vertex:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'({self.x},{self.y})'


for i in range(5):
    print(Vertex(random.randint(-100, 100), random.randint(-100, 100)))