import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
        
    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(
            screen,
            "white",
            (int(self.position.x), int(self.position.y)),
            self.radius,
            LINE_WIDTH,
        )
    
    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return []
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        asteroid_movement_1 =self.velocity.rotate(angle)
        asteroid_movement_2 =self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        Asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        Asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        Asteroid_1.velocity = asteroid_movement_1 * 1.2
        Asteroid_2.velocity = asteroid_movement_2 * 1.2
        return [Asteroid_1, Asteroid_2]
