from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            n_car = Turtle(shape="square")         
            n_car.shapesize(1, 2)
            n_car.penup()
            n_car.color(random.choice(COLORS))
            rand_y = random.randint(-250, 250)
            n_car.goto(300, rand_y)
            self.all_cars.append(n_car)


    def move(self):     
        for car in self.all_cars:
            car.backward(self.car_speed)

    
    def lvl_up(self):
        self.car_speed += MOVE_INCREMENT

