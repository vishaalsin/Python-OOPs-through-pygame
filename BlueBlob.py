from Blob import Blob
import random

BLUE = (0, 0, 255)

class BlueBlob(Blob):
    def __init__(self,envHeight, envWidth):
        super().__init__(BLUE,envHeight, envWidth)

    def move(self):
        self.move_x = random.randrange(-5, 5)
        self.move_y = random.randrange(-5, 5)
        self.x += self.move_x
        self.y += self.move_y