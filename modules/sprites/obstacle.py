'''
Function:
    定义障碍物类
Author:
    Charles
微信公众号:
    Charles的皮卡丘
'''
import random
import pygame


'''선인장'''
class Cactus(pygame.sprite.Sprite):
    def __init__(self, imagepaths, position=(600, 147), sizes=[(40, 40), (40, 40)], **kwargs):
        pygame.sprite.Sprite.__init__(self)
        # 그림 가져오기
        self.images = []
        image = pygame.image.load(imagepaths[0])
        for i in range(3):
            self.images.append(pygame.transform.scale(image.subsurface((i*101, 0), (101, 101)), sizes[0]))
        image = pygame.image.load(imagepaths[1])
        for i in range(3):
            self.images.append(pygame.transform.scale(image.subsurface((i*68, 0), (68, 70)), sizes[1]))
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
    def __init__(self, imagepath, position, size=(46, 40), **kwargs):
        pygame.sprite.Sprite.__init__(self)
        # 그림 가져오기
        self.images = []
        image = pygame.image.load(imagepath)
        for i in range(2):
            self.images.append(pygame.transform.scale(image.subsurface((i*92, 0), (92, 81)), size))
        self.image_idx = 0
        self.image = self.images[self.image_idx]
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.centery = position
        self.mask = pygame.mask.from_surface(self.image)
        # 필요한 변수들 정의
        self.speed = -10
        self.refresh_rate = 10
        self.refresh_counter = 0
    '''화면에 그리기'''
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    '''업데이트'''
    def update(self):
        if self.refresh_counter % self.refresh_rate == 0:
            self.refresh_counter = 0
            self.image_idx = (self.image_idx + 1) % len(self.images)
            self.loadImage()
        self.rect = self.rect.move([self.speed, 0])
        if self.rect.right < 0:
            self.kill()
        self.refresh_counter += 1
    '''현재 상태의 그림 불러오기'''
    def loadImage(self):
        self.image = self.images[self.image_idx]
        rect = self.image.get_rect()
        rect.left, rect.top = self.rect.left, self.rect.top
        self.rect = rect
        self.mask = pygame.mask.from_surface(self.image)

#사과(아이템, 먹으면 50점 추가)
class Apple(pygame.sprite.Sprite):
    def __init__(self, imagepath, position, size=(46, 40), **kwargs):
        pygame.sprite.Sprite.__init__(self)
        #그림 가져오기
        self.images = []
        image = pygame.image.load(imagepath)
        #사과가 5개 모양으로 돌아갈 수 있게 / 이미지 파일은 405 * 81 크기의 도트 그림으로 그리기
        #사과의 한 프레임당 81픽셀의 정사각형으로 그린다.
        for i in range(5):
            self.images.append(pygame.transform.scale(image.subsurface((81*i, 0), (81, 81)), size))
        self.image_idx = 0
        self.image = self.images[self.image_idx]
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.centery = position
        self.mask = pygame.mask.from_surface(self.image)
        #필요한 변수 정의
        self.speed = -10
        self.refresh_rate = 10
        self.refresh_counter = 0
    #그리기
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    
    #업데이트
    def update(self):
        if self.refresh_counter % self.refresh_rate == 0:
            self.refresh_counter = 0
            self.image_idx = (self.image_idx + 1) % len(self.images)
            self.loadImage()
        self.rect = self.rect.move([self.speed, 0])
        if self.rect.right < 0:
            self.kill()
        self.refresh_counter += 1
    
    #그림 불러오기
    def loadImage(self):
        self.image = self.images[self.image_idx]
        rect = self.image.get_rect()
        rect.left, rect.top = self.rect.left, self.rect.top
        self.rect = rect
        self.mask = pygame.mask.from_surface(self.image)
    
        