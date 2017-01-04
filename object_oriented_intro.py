import pygame
import random

STARTING_BLUE_BLOBS = 10
STARTING_RED_BLOBS = 3

WIDTH = 800
HEIGHT = 600
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
RED = (255,0,0)

game_display = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Blob World")
clock = pygame.time.Clock()

#based on intermediate ep 14 this seems optional?  weird but we'll include it.
pygame.init()


class Blob:

    #called dunder init method
    def __init__(self, color):
        self.x = random.randrange(0,WIDTH)
        self.y = random.randrange(0, HEIGHT)
        self.size = random.randrange(4,8)
        self.color = color

    def move(self):
        #the upper bound on randrange is NOT included.  so a <= x < b
        self.move_x = random.randrange(-1,2)
        self.move_y = random.randrange(-1,2)
        #print(self.move_x, self.move_y)
        self.x += self.move_x
        self.y += self.move_y

        if self.x < 0:
            self.x = 0
        elif self.x > WIDTH:
            self.x = WIDTH

        if self.y < 0:
            self.y = 0
        elif self.y > HEIGHT:
            self.y = HEIGHT


def draw_environment(blob_group_list):
    game_display.fill(WHITE)

    for blob_dict in blob_group_list:
        for blob_id in blob_dict:
            blob = blob_dict[blob_id]
            pygame.draw.circle(game_display, blob.color, [blob.x, blob.y], blob.size)
            blob.move()

    pygame.display.update()


def main():
    #red_blob = Blob(RED)

    #list comprehension and give the blobs an id
    blue_blobs = dict(enumerate([Blob(BLUE) for i in range(STARTING_BLUE_BLOBS)]))
    red_blobs = dict(enumerate([Blob(RED) for i in range(STARTING_RED_BLOBS)]))


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        draw_environment([blue_blobs, red_blobs])
        clock.tick(60)
        #print(red_blob.x, red_blob.y)

if __name__ == '__main__':
    main()