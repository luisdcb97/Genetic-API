from genetic.population import Population, Element
from physics.vector import Vector
import turtle
import math


class VisualElement(Element):
    def show(self, turt: turtle.Turtle):
        heading = math.degrees(self.velocity.angle())
        base = 8
        height = 20
        side = math.sqrt((base / 2) ** 2 + height ** 2)
        angle = math.degrees(math.asin(height / side))
        turt.penup()
        turt.goto(self.position.x, self.position.y)
        turt.pendown()
        turt.setheading(heading)
        turt.right(90)
        turt.forward(base / 2)
        turt.left(180 - angle)
        turt.forward(side)
        turt.left(2 * angle)
        turt.forward(side)
        turt.left(180 - angle)
        turt.forward(base / 2)


class VisualPopulation(Population):
    def __init__(self, size):
        super().__init__(size)
        self.elements = [VisualElement() for _ in range(size)]

    def update(self, turt):
        super().update()
        for elem in self.elements:
            elem.show(turt)


if __name__ == "__main__":
    t = turtle.Turtle()
    pop = VisualPopulation(5)
    for elem in pop.elements:
        elem.velocity = Vector.random()
    pop.update(t)

    turtle.mainloop()
