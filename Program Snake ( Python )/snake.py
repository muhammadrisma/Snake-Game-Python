import turtle
from turtle import *
from random import randrange
from freegames import square, vector


win = turtle.Screen()
win.title("Snake Game")
win.bgcolor("#383d52")
win.setup(width=600,height=600)
win.tracer(0)


food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)


def change(x, y):
    "Mengubah arah snake"
    aim.x = x
    aim.y = y

def inside(head):
    "True dalam bondaries"
    return -200 < head.x < 190 and -200 < head.y < 190
    

def move():
    "Move snake "
    head = snake[-1].copy()
    head.move(aim)

    
    
    if not inside(head) or head in snake:
        square(head.x, head.y, 80, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10

    else:
        snake.pop(0)


    clear()

    for body in snake:
        square(body.x, body.y, 10, '#01fe87')

    square(food.x, food.y, 10, 'red')
    update()
    ontimer(move, 100)


hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()

done()