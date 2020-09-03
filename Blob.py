import random

class Blob:

    def __init__(self,color,envHeight, envWidth):
        self.x = random.randrange(0,envHeight)
        self.y = random.randrange(0,envWidth)
        self.color = color
        self.size = random.randrange(4, 8)
        self.envHeight = envHeight
        self.envWidth = envWidth

    def move(self):
        self.move_x = random.randrange(-5,5)
        self.move_y = random.randrange(-5,5)
        self.x += self.move_x
        self.y += self.move_y

    def enforceBounds(self):
        if self.x < 0:
            self.x = 0
        elif self.x > self.envWidth:
            self.x = self.envWidth

        if self.y < 0:
            self.y = 0
        elif self.y > self.envHeight:
            self.y = self.envHeight

    def __mul__(self, other):
        if(self.size > 0 and other.size > 0):
            if self.size > other.size:
                other.size -= 1
            else:
                self.size -= 1