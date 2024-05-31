import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

chick = Player()
car = CarManager() 
score = Scoreboard()

screen.listen()
screen.onkeypress(chick.go_up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move()
  
    #Detect collision with cars
    for car1 in car.all_cars:
        if car1.distance(chick) < 20:
            game_is_on = False
            score.game_over()
        


    #Detect successful crosing
    if chick.crossed_line():
        chick.start_position()
        car.lvl_up()
        score.increase_lvl()

screen.exitonclick()
            