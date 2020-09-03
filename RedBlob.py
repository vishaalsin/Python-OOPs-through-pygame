from Blob import Blob

RED = (255, 0, 0)

class RedBlob(Blob):
    def __init__(self,envHeight, envWidth):
        super().__init__(RED,envHeight, envWidth)