import random
from turtle import Turtle,Screen
screen=Screen()
screen.setup(500,400)

y_positions=[-70,-40,-10,20,50,80]
colours=["red","orange","yellow","green","blue","purple"]
all_turtles=[]
is_race_on=False
user_bet=screen.textinput("Make your bet","which turtle will win the race: ")

for i in range(6):
    new_tim = Turtle("turtle")
    new_tim.penup()
    new_tim.goto(x=-230, y=y_positions[i])
    new_tim.color(colours[i])
    all_turtles.append(new_tim)
if user_bet:
    is_race_on=True
while is_race_on:
    for racer in all_turtles:
        if racer.xcor()>230:
            is_race_on=False
            winner=racer.pencolor()
            if winner==user_bet:
                print(f"You've won! The {winner} turtle is the winner!")
            else:
                print(f"You've lost! The {winner} turtle is the winner!")
        rand_distance=random.randint(0,10)
        racer.forward(rand_distance)


screen.exitonclick()