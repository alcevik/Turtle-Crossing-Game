from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

# Create a turtle player that starts at the bottom of the screen and listen
# for the "Up" keypress to move the turtle north.


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('green')
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def go_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    # return the turtle to the starting position and increase the speed of
    # the cars. Hint: think about creating an attribute and using the
    # MOVE_INCREMENT to increase the car speed.

    def go_to_start(self):
        self.goto(STARTING_POSITION)





