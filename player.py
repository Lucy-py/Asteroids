import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, PLAYER_SPEED, PLAYER_TURN_SPEED, PLAYER_RADIUS

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        
        self.rotation = 0
                
    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(
            screen,
            "white",
            self.triangle(),
            LINE_WIDTH,
        )

    def rotate(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotation -= dt * PLAYER_TURN_SPEED
        if keys[pygame.K_d]:
            self.rotation += dt * PLAYER_TURN_SPEED

    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]or keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w] or keys[pygame.K_s]:
            self.move(dt)

    
    def move(self, dt: float) -> None:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            forward = pygame.Vector2(0, 1).rotate(self.rotation)
            self.position += forward * dt * PLAYER_SPEED
        if keys[pygame.K_s]:
            forward = pygame.Vector2(0, 1).rotate(self.rotation)
            self.position -= forward * dt * PLAYER_SPEED