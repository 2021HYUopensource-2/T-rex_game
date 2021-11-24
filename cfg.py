#설정파일
import os


#화면크기
SCREENSIZE = (600, 150)
#FPS(속도)
FPS = 60
#오디오 파일 위치
AUDIO_PATHS = {
    'die': os.path.join(os.getcwd(), 'resources/audios/die.wav'),
    'jump': os.path.join(os.getcwd(), 'resources/audios/jump.wav'),
    'point': os.path.join(os.getcwd(), 'resources/audios/point.wav'),
    'bgm': os.path.join(os.getcwd(), 'resources/audios/bgm.mp3'),
    'bgm_level2': os.path.join(os.getcwd(), 'resources/audios/bgm_level2.mp3'),
    'bgm_level3': os.path.join(os.getcwd(), 'resources/audios/bgm_level3.mp3'),
    'bgm_level4': os.path.join(os.getcwd(), 'resources/audios/bgm_level4.mp3')
}
#그림 파일 위치
IMAGE_PATHS = {
    'cacti': [
        os.path.join(os.getcwd(), 'resources/images/cacti-big.png'),
        os.path.join(os.getcwd(), 'resources/images/cacti-small.png')
    ],
    'cloud': os.path.join(os.getcwd(), 'resources/images/cloud.png'),
    'dino': [
        os.path.join(os.getcwd(), 'resources/images/dino.png'),
        os.path.join(os.getcwd(), 'resources/images/dino_ducking.png')
    ],
    'gameover': os.path.join(os.getcwd(), 'resources/images/gameover.png'),
    'ground': os.path.join(os.getcwd(), 'resources/images/ground.png'),
    'numbers': os.path.join(os.getcwd(), 'resources/images/numbers.png'),
    'ptera': os.path.join(os.getcwd(), 'resources/images/ptera.png'),
    'replay': os.path.join(os.getcwd(), 'resources/images/replay.png')
}
#배경색상
BACKGROUND_COLOR = (235, 235, 235)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
