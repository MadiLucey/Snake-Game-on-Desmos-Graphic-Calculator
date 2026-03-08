import casioplot
import random
import time
import keyboard

WIDTH = 128
HEIGHT = 64
SIZE = 4

snake = [(40, 30)]
direction = (SIZE, 0)

food = (random.randrange(0, WIDTH, SIZE), random.randrange(0, HEIGHT, SIZE))

def draw_square(x, y):
    for i in range(SIZE):
        for j in range(SIZE):
            casioplot.set_pixel(x+i, y+j, (0,0,0))

while True:

    casioplot.clear_screen()

    # controls
    if keyboard.is_pressed("left"):
        direction = (-SIZE,0)
    if keyboard.is_pressed("right"):
        direction = (SIZE,0)
    if keyboard.is_pressed("up"):
        direction = (0,-SIZE)
    if keyboard.is_pressed("down"):
        direction = (0,SIZE)

    head = snake[0]
    new_head = (head[0] + direction[0], head[1] + direction[1])

    snake.insert(0, new_head)

    if new_head == food:
        food = (random.randrange(0, WIDTH, SIZE), random.randrange(0, HEIGHT, SIZE))
    else:
        snake.pop()

    # draw snake
    for segment in snake:
        draw_square(segment[0], segment[1])

    # draw food
    draw_square(food[0], food[1])

    casioplot.show_screen()
    time.sleep(0.15)
