#Создай собственный Шутер!
from random import randint
from pygame import *
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()

window = display.set_mode((700, 500))
background = transform.scale(image.load('galaxy.jpg'),(700, 500))
class GameSprite(sprite.Sprite):
    def __init__(self, image_player, speed, x, y, width, height):
        super().__init__()
        self.image = transform.scale(image.load(image_player), (width, height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        elif keys_pressed[K_d] and self.rect.x < 600:
            self.rect.x += self.speed
    def shoot(self):
        bullet = Bullet('bullet.png', speed=6,x=self.rect.centerx, y=self.rect.y, width=15, height=20)
        bullets.add(bullet)        

rocket = Player(image_player='rocket.png', speed=12, x=0, y=320, width = 70, height = 150)

class Enemy(GameSprite):

    def update(self):
        global lose
        self.rect.y += self.speed
        if self.rect.y >= 450:
            self.rect.y = -20
            self.rect.x = randint(0, 550)
            lose += 1

class Bullet(GameSprite):
    def update(self):
        self.rect.y-=self.speed
        if self.rect.y < 0:
            self.kill()

boss =  Enemy(image_player='ufo.png', speed=1, x=randint(0,600), y=0, width = 160, height = 100)
ufos = sprite.Group()
for i in range(5):
    ufo = Enemy(image_player='ufo.png', speed=randint(1, 2), x=randint(0,600), y=0, width = 80, height = 50)
    ufos.add(ufo)
asteroids = sprite.Group()
for i in range(3):
    astr = Enemy(image_player='asteroid.png', speed=1, x=randint(0,600), y=0, width = 50, height = 30)
    asteroids.add(astr)

bullets = sprite.Group()

score = 0
lose = 0
life_score = 0



finish = False

#шифты и надписи
font.init()
font2 = font.SysFont('Arial', 36)
color3 = (0, 255, 0)  
color2 = (180, 200, 0)
color1 = (255, 0, 0)  
fps = 60
clock = time.Clock()
win_text = font2.render('Ты выйграл', True, (255,255,255))
lose_text = font2.render('Ты проиграл', True, (255,255,255))
game = True
while game:
    for i in event.get():
        if i.type == QUIT:
            game = False
        if i.type == KEYDOWN:
            if i.key == K_SPACE:
                rocket.shoot()

    if not finish:

        score_text = font2.render('Счет:'+ str(score), True, (255,255,255))
        miss_text = font2.render('Пропущено:'+ str(lose), True, (255,255,255))
        life_text = font2.render(''+ str(life_score), True, (255,255,255))
        if life_score == 1:
            life_text = font2.render(''+ str(life_score), True, color3)
        elif life_score == 2:
            life_text = font2.render(''+ str(life_score), True, color2)
        elif life_score == 3:
            life_text = font2.render(''+ str(life_score), True, color1)

        window.blit(background, (0,0))
        window.blit(score_text, (50,30))
        window.blit(miss_text, (50,60))
        window.blit(life_text, (650, 30))
        rocket.update()
        rocket.reset()

        bullets.update()
        bullets.draw(window) 

        asteroids.update()
        asteroids.draw(window) 

        ufos.update()
        ufos.draw(window)

        if sprite.groupcollide(ufos , bullets, True, True):
            score += 1
            ufo = Enemy(image_player='ufo.png', speed=randint(1, 3), x=randint(0,600), y=0, width = 80, height = 50)
            ufos.add(ufo)
        if score > 10:
            boss.reset()
            boss.update()
            if sprite.spritecollide(boss, bullets, True):
                window.blit(win_text, (250, 250))
                finish = True



        if life_score >= 3:
            finish = True

        if sprite.spritecollide(rocket, ufos, True) or sprite.spritecollide(rocket, asteroids, True):
            life_score += 1
        if lose >= 10:
            finish = True

            window.blit(lose_text, (250, 250))


    display.update()
    clock.tick(fps)