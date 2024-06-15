from turtle import Turtle, Screen
import random
# daw = Turtle()
screen = Screen()

# def move_forwards():
#     daw.fd(10)

# def move_backwards():
#     daw.bk(10)

# def turn_clockwise():
#     new_heading = daw.heading() - 10              #Another way
#     daw.setheading(new_heading)                   # daw.right(10)
#                                                   # daw.heading()
# def turn_anticlockwise():
#     new_heading = daw.heading() + 10              # daw.left(10)
#     daw.setheading(new_heading)                   # daw.heading

# def back_to_the_start():
#     daw.home()
#     daw.clear()

# screen.onkeypress(key='w', fun=move_forwards)
# screen.onkeypress(key='s', fun=move_backwards)
# screen.onkeypress(key='d', fun=turn_clockwise)
# screen.onkeypress(key='a', fun=turn_anticlockwise)
# screen.onkey(key='c', fun=back_to_the_start)


#Turtle race

is_race_on = False
y_positions = [-70, -40, -10, 20, 50, 80]
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'pink']
screen.setup(width=1000, height=400)
user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color(red, orange, yellow, green, blue, pink): ')
all_turtle = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[turtle_index])
    new_turtle.up()
    new_turtle.goto(x=-480, y=y_positions[turtle_index])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    
    for turtle in all_turtle:
        if turtle.xcor() >= 480:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f'You\'ve won! The {winning_color} turtle is the winner!')
            else:
                print(f'You\'ve lost! The {winning_color} turtle is the winner!')            
            
        
        random_distance = random.randint(0, 10)
        turtle.fd(random_distance)
        


screen.exitonclick()