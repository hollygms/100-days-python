from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10 #how much cars speed up with each level, add it to move distance
number_of_cars = 10
cars = []



class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.cars = []
        self.make_cars()

    def move(self, level):
        for car in self.cars:
            car.setx(car.xcor() - (STARTING_MOVE_DISTANCE + (MOVE_INCREMENT * level)))
            if car.xcor() < -310:
                car.setx(random.randint(320, 350))
                car.sety(random.randint(-260, 260))

    def make_cars(self):
        for _ in range(number_of_cars):
            car = Turtle(shape="square")
            car.penup()
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.color(random.choice(COLORS))
            self.cars.append(car)
            car.goto(random.randint(-300, 300), random.randint(-260, 260))






