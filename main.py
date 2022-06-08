from turtle import Turtle, Screen
from random import randint


screen=Screen()
screen.setup(width=500, height=400)
is_race_on = False
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
move =[1, 2, 3, 4, 5]
all_turtles = []

for turtle_index in range(0, 6):
    tim=Turtle(shape="turtle")
    tim.penup()
    tim.goto(x=-230, y=y_positions[turtle_index])
    tim.color(colors[turtle_index])
    all_turtles.append(tim)

if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.color()
            if winning_color == user_bet:
                print(f"You have won! The {winning_color} turtle is the winner")
            else:
                print(f"You have lost! The {winning_color} turtle is the winner")

        rand_distance = randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()