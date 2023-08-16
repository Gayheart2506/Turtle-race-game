from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

colors = ["red", "purple", "yellow", "green", "pink", "blue"]
stake_bet = screen.textinput(title="Race bet", prompt="Which turtle will win the race (red, purple , yellow , green, "
                                                      "pink , "
                                                      "blue )? Enter a color : ").lower()
y_coordinates = [-100, -60, -20, 20, 60, 100]
move_turtle = False
total_turtles = []
for number_of_turtles in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[number_of_turtles])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_coordinates[number_of_turtles])
    total_turtles.append(new_turtle)

if stake_bet:
    move_turtle = True

while move_turtle:

    for turtles in total_turtles:
        if turtles.xcor() > 230:
            move_turtle = False
            win_color = turtles.pencolor()
            if stake_bet == win_color:
                print(f"User's bet : {stake_bet}")
                print(f"Congratulations {win_color} turtle won the race , you've won the bet.")
            else:
                print(f"User's bet : {stake_bet}")
                print(f"You've lost the bet , {win_color} turtle won the race.")

        number_of_moves = random.randint(0, 10)
        turtles.forward(number_of_moves)

# tim = Turtle(shape="turtle")
# ucal = Turtle(shape="turtle")
# emma = Turtle(shape="turtle")
# kister = Turtle(shape="turtle")
# louis = Turtle(shape="turtle")
#
# gay.penup()
# gay.goto(x=-230, y=-100)
#
# tim.penup()
# tim.goto(x=-230, y=-60)
#
# ucal.penup()
# ucal.goto(x=-230, y=-20)
#
# emma.penup()
# emma.goto(x=-230, y=20)
#
# kister.penup()
# kister.goto(x=-230, y=60)
#
# louis.penup()
# louis.goto(x=-230, y=100)

screen.exitonclick()
