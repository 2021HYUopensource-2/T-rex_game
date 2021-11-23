'''
Function:
    크롬 공룡 게임
Author:
    Charles
'''
import cfg
import sys
import random
import pygame
from modules import *



'''main'''
def main(highest_score):
    # 게임초기화
    pygame.init()
    screen = pygame.display.set_mode(cfg.SCREENSIZE)
    pygame.display.set_caption('T-Rex Rush')
    #모든 소리파일 가져오기
    sounds = {}
    for key, value in cfg.AUDIO_PATHS.items():
        sounds[key] = pygame.mixer.Sound(value)
        # 위 코드가 음성값 할당 해줌.(창)
    # 게임 시작화면
    GameStartInterface(screen, sounds, cfg)
    # 게임에 필요한 요소와 변수들 정의
    score = 0
    score_board = Scoreboard(cfg.IMAGE_PATHS['numbers'], position=(534, 15), bg_color=cfg.BACKGROUND_COLOR)
    highest_score = highest_score
    print(highest_score)
    highest_score_board = Scoreboard(cfg.IMAGE_PATHS['numbers'], position=(435, 15), bg_color=cfg.BACKGROUND_COLOR, is_highest=True)
    dino = Dinosaur(cfg.IMAGE_PATHS['dino'])

    ground = Ground(cfg.IMAGE_PATHS['ground'], position=(0, cfg.SCREENSIZE[1]))
    cloud_sprites_group = pygame.sprite.Group()
    cactus_sprites_group = pygame.sprite.Group()
    ptera_sprites_group = pygame.sprite.Group()
    add_obstacle_timer = 0
    score_timer = 0
    # 게임 루프
    clock = pygame.time.Clock()

    #음악구현(1)
    BGM = pygame.mixer.Sound("resources/audios/bgm.mp3")
    BGM_level2 = pygame.mixer.Sound("resources/audios/bgm_level2.mp3")
    BGM_level3 = pygame.mixer.Sound("resources/audios/bgm_level3.mp3")
    #구현 끝

        
    while True:
        #배경음악 구현(2) 0 200 300 500 1000 각각 음악.
        if(score <=5):
            BGM_level2.stop()
            BGM.play(-1)
        if(score >50): # 임의로 100 설정. 합의하에 값 조절.
            BGM.stop()
            BGM_level2.play(-1)
        if(score >100):
            BGM_level2.stop()
            BGM_level3.play(-1)
        #구현 끝

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                    dino.jump(sounds)
                elif event.key == pygame.K_DOWN:
                    dino.duck()
            elif event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
                dino.unduck()
        screen.fill(cfg.BACKGROUND_COLOR)
        # --무작위 구름 추가
        if len(cloud_sprites_group) < 5 and random.randrange(0, 300) == 10:
            cloud_sprites_group.add(Cloud(cfg.IMAGE_PATHS['cloud'], position=(cfg.SCREENSIZE[0], random.randrange(30, 75))))
        # --선인장/익룡 무작위 추가
        add_obstacle_timer += 1
        if add_obstacle_timer > random.randrange(50, 150):
            add_obstacle_timer = 0
            random_value = random.randrange(0, 10)
            if random_value >= 5 and random_value <= 7:
                cactus_sprites_group.add(Cactus(cfg.IMAGE_PATHS['cacti']))
            else:
                position_ys = [cfg.SCREENSIZE[1]*0.82, cfg.SCREENSIZE[1]*0.75, cfg.SCREENSIZE[1]*0.60, cfg.SCREENSIZE[1]*0.20]
                ptera_sprites_group.add(Ptera(cfg.IMAGE_PATHS['ptera'], position=(600, random.choice(position_ys))))
        # --게임 요소 업데이트
        dino.update()
        ground.update()
        cloud_sprites_group.update()
        cactus_sprites_group.update()
        ptera_sprites_group.update()
        score_timer += 1
        if score_timer > (cfg.FPS//12):
            score_timer = 0
            score += 1
            score = min(score, 99999)
            if score > highest_score:
                highest_score = score
            if score % 100 == 0:
                sounds['point'].play()
            if score % 1000 == 0:
                ground.speed -= 1
                for item in cloud_sprites_group:
                    item.speed -= 1
                for item in cactus_sprites_group:
                    item.speed -= 1
                for item in ptera_sprites_group:
                    item.speed -= 1
        # --충돌 체크
        for item in cactus_sprites_group:
            if pygame.sprite.collide_mask(dino, item):
                dino.die(sounds)
        for item in ptera_sprites_group:
            if pygame.sprite.collide_mask(dino, item):
                dino.die(sounds)
        # --게임 요소 화면에 그리기
        dino.draw(screen)
        ground.draw(screen)
        cloud_sprites_group.draw(screen)
        cactus_sprites_group.draw(screen)
        ptera_sprites_group.draw(screen)
        score_board.set(score)
        highest_score_board.set(highest_score)
        score_board.draw(screen)
        highest_score_board.draw(screen)
        # --화면 업데이트
        pygame.display.update()
        clock.tick(cfg.FPS)
        # --게임 종료 여부 체크
        if dino.is_dead:
            BGM.stop()
            BGM_level2.stop()
            BGM_level3.stop()
            break
        
    # 게임 종료 인터페이스
    return GameEndInterface(screen, cfg), highest_score


#최종 실행
if __name__ == '__main__':
    highest_score = 0
    while True:
        flag, highest_score = main(highest_score)
        if not flag: break
