import pygame
from pygame.math import Vector2 

from random import randint


BOIDS_AMOUNT = 14
CLOSENESS_DISTANCE = 20
MAX_VELOCITY = 3


class Boid:
  def __init__(self, position):
    self.position = Vector2(position)
    self.velocity = Vector2()

  def update(self, frame_time_ms):
    pass

  def limit_velocity(self):
    self.velocity = self.velocity.normalize() * MAX_VELOCITY

  def bound_position(self):
    if self.position.x < 0:
      self.velocity.x = 10
    elif self.position.x > 640:
      self.velocity.x = -10
    if self.position.y < 0:
      self.velocity.y = 10
    elif self.position.y > 420:
      self.velocity.y = -10

  def draw(self, surface):
    pygame.draw.circle(surface, (255, 0, 0), self.position, 2)

class Flock:

  def __init__(self):
    self.boids = [Boid((randint(0, 640), randint(0, 420))) for _ in range(BOIDS_AMOUNT)]

  def update(self):
    for boid in self.boids:
      v1 = self._rule1(boid)
      v2 = self._rule2(boid)
      v3 = self._rule3(boid)

      boid.velocity += v1 + v2 + v3
      boid.bound_position()
      boid.limit_velocity()
      
      boid.position += boid.velocity

  def _rule1(self, boid):
    # flying towards center of the flock
    mc = Vector2()
    for b in self.boids:
      if b is not boid:
        mc += b.position
    mc /= BOIDS_AMOUNT - 1
    return (mc - boid.position) / 100

  def _rule2(self, boid):
    # flying away from nearest boids
    c = Vector2()
    for b in self.boids:
      if b is not boid:
        if (b.position - boid.position).magnitude() < CLOSENESS_DISTANCE:
          c -= b.position - boid.position
    return c

  def _rule3(self, boid):
    # flying in the same direction
    pv = Vector2()
    for b in self.boids:
      if b is not boid:
        pv += b.velocity
    pv /= BOIDS_AMOUNT - 1
    return (pv - boid.velocity) / 8

  def draw(self, surface):
    for boid in self.boids:
      boid.draw(surface)
  