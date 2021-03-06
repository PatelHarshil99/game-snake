import turtle
import time
import random

delay = 0.1

score = 0
high_score = 0

wn = turtle.Screen()
wn.title("snake Game by HARSHIL")
wn.bgcolor("white")
wn.setup(width=600, height=600)
wn.tracer(0)

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("blue")
food.penup()
food.goto(0,100)


segments = []

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("green")
pen.penup()
pen.hideturtle()
pen.goto(0, 270)
pen.write("Score: 0   High score: 0", align="center", font=("Courier", 22, "normal"))

point = turtle.Turtle()
point.speed(0)
point.shape("square")
point.color("red")
point.penup()
point.hideturtle()



def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"   

def move():
    if head.direction == "up" :
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down" :
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left" :
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right" :
        x = head.xcor()
        head.setx(x + 20)


wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")



while True:
    wn.update()

    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        point.goto(0, 0)
        point.write("GAME OVER", align="center", font=("Courier", 22, "normal"))
        time.sleep(1)
        point.clear()
        head.goto(0, 0)
        head.direction = "stop"

        for segment in segments:
            segment.goto(1000, 1000)

        segments.clear()

        score = 0

        delay = 0.1

        pen.clear()
        pen.write("Score: {}  High score: {}".format(score, high_score), align="center", font=("Courier", 22, "normal"))


    if head.distance(food) < 15:
        x = random.randint(-290, 260)
        y = random.randint(-290, 260)
        food.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        delay -= 0.001

        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {}  High score: {}".format(score, high_score), align="center", font=("Courier", 22, "normal"))

    for index in range (len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        segments[0].goto(head.xcor(), head.ycor())     

    move()

    for segment in segments:
        if segment.distance(head) < 15:
            point.goto(0, 0)
            point.write("GAME OVER", align="center", font=("Courier", 22, "normal"))
            time.sleep(1)
            point.clear()
            head.goto(0, 0)
            head.direction = "stop"

            for segment in segments:
                segment.goto(1000, 1000)

            segments.clear()

            score = 0

            delay = 0.1
        
            pen.clear()
            pen.write("Score: {}  High score: {}".format(score, high_score), align="center", font=("Courier", 22, "normal"))
  

    time.sleep(delay)

wn.mainloop()