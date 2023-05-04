from turtle import Turtle, Screen
import random

is_race_on=False 
screen=Screen()

screen.setup(height=500, width=500)
user_bet=screen.textinput(title="Make your bet", prompt="Which turtle win the race? Enter a color: ")
print(user_bet)

colours=["skyblue", "sienna", "yellow", "purple", "blue", "red", "tan"]
y_position=[100,-100,50,-50,0,-150,150]

all_turtles=[]
 
for turtle_index in range(7):
    dim=Turtle(shape="turtle")
    dim.penup()
    dim.goto(x=-230,y=y_position[turtle_index])
    dim.color(colours[turtle_index])
    all_turtles.append(dim)
    
    
if user_bet:
    is_race_on=True
    
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race_on=False
            winning_color =turtle.pencolor()
            if winning_color==user_bet:
                print(f"You have won! The {winning_color} turtle won the race.")
            else:
                print(f"You have lost! The {winning_color} turtle won the race. ")
    
        random_move=random.randint(1,10)
        turtle.forward(random_move)
        



screen.exitonclick()