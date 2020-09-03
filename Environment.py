from BlueBlob import BlueBlob
from RedBlob import RedBlob
import numpy as np

import pygame


HEIGHT = 500
WIDTH = 500

NUM_RED_BLOBS = 20
NUM_BLUE_BLOBS = 10


WHITE = (255, 255, 255)
GREEN = (0, 0, 255)

game_display = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Blob World')
clock = pygame.time.Clock()


def handleCollisions(blobs):
    delset = set()
    for blob1 in blobs:
        for blob2 in blobs:
            if blob1 == blob2:
                pass
            else:
                handleCollision(delset,blobs,blob1,blob2)
    for id in delset:
        del blobs[id]

def handleCollision(delset,blobs,blob1_id,blob2_id):
    blob1 = blobs[blob1_id]
    blob2 = blobs[blob2_id]
    if collision(blob1, blob2):
        blob1*blob2
    if blob1.size <= 0:
        delset.add(blob1_id)
    if blob2.size <= 0:
        delset.add(blob2_id)


def collision(blob1, blob2):
    return np.linalg.norm(np.array([blob1.x, blob1.y]) - np.array([blob2.x, blob2.y])) < (blob1.size + blob2.size)


def draw_environment(blobs):
    game_display.fill(WHITE)
    for blob_id in blobs:
        blob = blobs[blob_id]
        pygame.draw.circle(game_display, blob.color, [blob.x, blob.y], blob.size)
        blob.move()
        blob.enforceBounds()
    blobs = handleCollisions(blobs)
    pygame.display.update()

def main():
    blobs = [RedBlob(HEIGHT, WIDTH) for i in range(NUM_RED_BLOBS)]
    blue_blobs = [BlueBlob(HEIGHT, WIDTH) for i in range(NUM_BLUE_BLOBS)]
    blobs = dict(enumerate(blobs+blue_blobs))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        draw_environment(blobs)
        clock.tick(60)


if __name__ == '__main__':
    main()

