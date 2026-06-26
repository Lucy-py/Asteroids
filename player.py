import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        
        self.rotation = 0
        self.shot_cooldown = 0
        self.score = 0
        self.lives = 3
        self.damage_cooldown = 0
                
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
            "green",
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
        
        if keys[pygame.K_SPACE]:
            self.shoot()

        self.shot_cooldown -= dt
        self.damage_cooldown -= dt
    
    def move(self, dt: float) -> None:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            forward = pygame.Vector2(0, 1).rotate(self.rotation)
            self.position += forward * dt * PLAYER_SPEED
        if keys[pygame.K_s]:
            forward = pygame.Vector2(0, 1).rotate(self.rotation)
            self.position -= forward * dt * PLAYER_SPEED

    def shoot(self):
        if self.shot_cooldown <= 0:
            self.shot_cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS
            return Shot(self.position.x, self.position.y, pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED)
        
    def score_add(self, modifier: int) -> None:
        self.score += DEFAULT_POINTS // modifier

    def score_subtract(self) -> None:
        self.score -= DEFAULT_POINTS
        if self.score < 0:
            self.score = 0


    def alive_check(self) -> None:
        if self.lives <= 0:
            return False
        return True

    def take_damage(self) -> None:
        if self.damage_cooldown <= 0:
            self.lives -= 1
            self.damage_cooldown = PLAYER_DAMAGE_COOLDOWN_SECONDS
            print("hit")