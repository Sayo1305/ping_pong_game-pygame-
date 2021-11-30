import sys
import pygame
from pygame import display
from pygame import key
from pygame.locals import*
from pygame import font

#initotialize the game
pygame.init()

#screen size(height and width)
screen_wi = 600
screen_hi = 500

#frame per second
fps = pygame.time.Clock()

#screen making
screen = pygame.display.set_mode((screen_wi,screen_hi))
pygame.display.set_caption("ping pong pooo!!!!")

#font
font10 = pygame.font.SysFont('constantia',10)
font20 = pygame.font.SysFont('constantia',20)
font30 = pygame.font.SysFont('constantia',30)
font40 = pygame.font.SysFont('constantia',40)
#game variable
margin = 50
cpu_score = 0
player_score = 0
winner = 0
life_ball = False
speed_increase = 0
#color
red = [255,0,0]
green = [0,255,0]
white = [255,255,255]
black = [0,0,0]
crimson = [220,20,60]
salmon = [250,128,114]
turquoise = [64,224,208]
dark_blue = [0,0,139]
lime = [0,255,0]


#draw the main screen
def draw_board():
    screen.fill(turquoise)
    pygame.draw.line(screen,white,(0,50),(screen_wi,margin),3)

#function to draw the text 
def print(text,font,color,x,y):
    img = font.render(text,True,color)
    screen.blit(img,(x,y))

#class for paddle
class paddle():
    def __init__(self,x,y,col):
        self.x = x
        self.y = y
        self.rect = Rect(self.x,self.y,20,100)
        self.speed = 5
        self.color = col
    def move(self):
        key = pygame.key.get_pressed()
        if(key[pygame.K_UP] and self.rect.top > margin):
            self.rect.move_ip(0,-1 * self.speed)
        if(key[pygame.K_DOWN] and self.rect.bottom < screen_hi):
            self.rect.move_ip(0,self.speed )
    def draw(self):
        pygame.draw.rect(screen,self.color,self.rect)
    def ai(self):
        if self.rect.centery < pong.rect.top and self.rect.bottom < screen_hi:
            self.rect.move_ip(0, self.speed)
	    #move up
        if self.rect.centery > pong.rect.bottom and self.rect.top > margin:
            self.rect.move_ip(0, -1 * self.speed)


#class for ball
class ball():
	def __init__(self, x, y):
		self.reset(x, y)
	def move(self):

		#check collision with top margin
		if self.rect.top < margin:
			self.speed_y *= -1
		#check collision with bottom of the screen
		if self.rect.bottom > screen_hi:
			self.speed_y *= -1
		if self.rect.colliderect(player_paddle) or self.rect.colliderect(cpu_paddle):
			self.speed_x *= -1
		#check for out of bounds
		if self.rect.left < 0:
			self.winner = 1
		if self.rect.left > screen_wi:
			self.winner = -1
		#update ball position
		self.rect.x += self.speed_x
		self.rect.y += self.speed_y
		return self.winner
	def draw(self):
		pygame.draw.circle(screen,salmon , (self.rect.x + self.ball_rad, self.rect.y + self.ball_rad), self.ball_rad)
	def reset(self, x, y):
		self.x = x
		self.y = y
		self.ball_rad = 8
		self.rect = Rect(x, y, self.ball_rad * 2, self.ball_rad * 2)
		self.speed_x = -4
		self.speed_y = 4
		self.winner = 0# 1 is the player and -1 is the CPU
player_paddle = paddle(screen_wi-40,screen_hi//2,dark_blue)
cpu_paddle = paddle(20,screen_hi//2,red)


#main loop of the game 

#create 
pong  = ball(screen_wi - 60,screen_hi // 2 + 50)
run = True


while run:
    fps.tick(60)
    draw_board()
    print(("CPU: "+ str(cpu_score)),font30,black,20,15)
    print(("PLAYER: "+ str(player_score)),font30,black,screen_wi - 150,15)
    print(("Ball speed: " + str(abs(pong.speed_x))) , (font30 ),black, screen_wi // 2 - 100,15)
    player_paddle.draw()
    cpu_paddle.draw()
    if(life_ball == True):
        speed_increase+=1
        winner = pong.move()
        if winner == 0:
            player_paddle.move()
            cpu_paddle.ai()
            pong.draw()
        else:
            life_ball = False
            if winner == 1:
                player_score+=1
            else:
                cpu_score+=1
    #print player intuvction
    key2 = pygame.key.get_pressed()
    if life_ball == False:
        if winner == 0:
            print("Press space_bar to continue",font30,black,100,screen_hi // 2 - 100)
        if winner == 1:
            print("You scored!!!",font30,green,100,screen_hi // 2 - 100)
            print("Press space_bar to continue",font30,black,100,screen_hi // 2 - 150)
        if winner == -1:
            print("Cpu scored!!!",font30,red,100,screen_hi // 2 - 100)
            print("Press space_bar to continue",font30,black,100,screen_hi // 2 - 150)
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            run = False
        if key2[pygame.K_SPACE] and life_ball == False:
            life_ball = True
            pong.reset(screen_wi - 60,screen_hi // 2 + 50)
    if speed_increase > 500:
        speed_increase = 0
        if(pong.speed_x < 0):
            pong.speed_x -= 1
        if pong.speed_x > 0:
            pong.speed_x +=1
        if(pong.speed_y < 0):
            pong.speed_y -= 1
        if pong.speed_y > 0:
            pong.speed_y +=1
    pygame.display.update()
pygame.quit()