from physics.vector import Vector, Number


class Element(object):
    def __init__(self, position: Vector=None, velocity: Vector=None):
        self.position: Vector = position \
            if position is not None else Vector.random()
        self.velocity: Vector = velocity \
            if velocity is not None else Vector.random()
        self.acceleration: Vector = Vector.zero()

    def apply_force(self, force: Vector):
        self.acceleration += force

    def update(self):
        self.velocity += self.acceleration
        self.position += self.velocity
        self.acceleration *= 0
