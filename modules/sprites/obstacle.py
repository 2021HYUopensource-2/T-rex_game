import random
import pygame

'''선인장'''


class Cactus(pygame.sprite.Sprite):
    def __init__(self, image_path, position=(600, 147)):
        pygame.sprite.Sprite.__init__(self)
        # 그림 가져오기
        self.images = []
        image = pygame.image.load(image_path[0])
        for i in range(3):
            self.images.append(pygame.transform.scale(image.subsurface((i * 101, 0), (101, 101)), (40, 40)))
        image = pygame.image.load(image_path[1])
        for i in range(3):
            self.images.append(pygame.transform.scale(image.subsurface((i * 68, 0), (68, 70)), (40, 40)))
        self.image = random.choice(self.images)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.bottom = position
        self.mask = pygame.mask.from_surface(self.image)
        # 필요한 변수 정의
        self.speed = -10

    '''화면에 그리기'''

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    '''업데이트'''

    def update(self):
        self.rect = self.rect.move([self.speed, 0])
        if self.rect.right < 0:
            self.kill()


'''익룡'''


class Ptera(pygame.sprite.Sprite):
    def __init__(self, image_path, position, size=(46, 40)):
        pygame.sprite.Sprite.__init__(self)
        # 그림 가져오기
        self.images = []
        image = pygame.image.load(image_path)
        for i in range(2):
            self.images.append(pygame.transform.scale(image.subsurface((i * 92, 0), (92, 81)), size))
        self.image_idx = 0
        self.image = self.images[self.image_idx]
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.centery = position
        self.mask = pygame.mask.from_surface(self.image)
        # 필요한 변수들 정의
        self.speed = -10
        self.refresh_rate = 11
        self.refresh_counter = 0

    '''화면에 그리기'''

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    '''업데이트'''

    def update(self):
        if self.refresh_counter % self.refresh_rate == 0:
            self.refresh_counter = 0
            self.image_idx = (self.image_idx + 1) % len(self.images)
            self.load_image()
        self.rect = self.rect.move([self.speed, 0])
        if self.rect.right < 0:
            self.kill()
        self.refresh_counter += 1

    '''현재 상태의 그림 불러오기'''

    def load_image(self):
        self.image = self.images[self.image_idx]
        rect = self.image.get_rect()
        rect.left, rect.top = self.rect.left, self.rect.top
        self.rect = rect
        self.mask = pygame.mask.from_surface(self.image)


# 사과
class Apple(pygame.sprite.Sprite):
    def __init__(self, image_path, position, size=(46, 40)):
        pygame.sprite.Sprite.__init__(self)
        # 그림 가져오기
        self.images = []
        image = pygame.image.load(image_path)
        for i in range(5):
            self.images.append(pygame.transform.scale(image.subsurface((i * 81, 0), (81, 81)), size))
        self.image_idx = 0
        self.image = self.images[self.image_idx]
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.centery = position
        self.mask = pygame.mask.from_surface(self.image)
        # 필요한 변수들 정의
        self.speed = -10
        self.refresh_rate = 11
        self.refresh_counter = 0

    '''화면에 그리기'''

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    '''업데이트'''

    def update(self):
        if self.refresh_counter % self.refresh_rate == 0:
            self.refresh_counter = 0
            self.image_idx = (self.image_idx + 1) % len(self.images)
            self.load_image()
        self.rect = self.rect.move([self.speed, 0])
        if self.rect.right < 0:
            self.kill()
        self.refresh_counter += 1

    '''현재 상태의 그림 불러오기'''

    def load_image(self):
        self.image = self.images[self.image_idx]
        rect = self.image.get_rect()
        rect.left, rect.top = self.rect.left, self.rect.top
        self.rect = rect
        self.mask = pygame.mask.from_surface(self.image)
