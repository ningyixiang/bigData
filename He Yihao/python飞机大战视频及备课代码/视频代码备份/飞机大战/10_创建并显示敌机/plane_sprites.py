import pygame

# 屏幕大小的常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 刷新的帧率
FRAME_PER_SEC = 60
# 创建敌机的定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT


class GameSprite(pygame.sprite.Sprite):
    """飞机大战游戏精灵"""

    def __init__(self, image_name, speed=1):

        # 调用父类的初始化方法
        super().__init__()

        # 定义对象的属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):

        # 在屏幕的垂直方向上移动
        self.rect.y += self.speed


class Background(GameSprite):
    """游戏背景精灵"""

    def __init__(self, is_alt=False):

        # 1. 调用父类方法实现精灵的创建(image/rect/speed)
        super().__init__("./images/background.png")

        # 2. 判断是否是交替图像，如果是，需要设置初始位置
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):

        # 1. 调用父类的方法实现
        super().update()

        # 2. 判断是否移出屏幕，如果移出屏幕，将图像设置到屏幕的上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):
    """敌机精灵"""

    def __init__(self):

        # 1. 调用父类方法，创建敌机精灵，同时指定敌机图片
        super().__init__("./images/enemy1.png")

        # 2. 指定敌机的初始随机速度

        # 3. 指定敌机的初始随机位置

    def update(self):

        # 1. 调用父类方法，保持垂直方向的飞行
        super().update()

        # 2. 判断是否飞出屏幕，如果是，需要从精灵组删除敌机
        if self.rect.y >= SCREEN_RECT.height:
            print("飞出屏幕，需要从精灵组删除...")
