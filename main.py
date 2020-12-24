import pygame, sys, random

pos = 0 

def base_movement():
	screen.blit(base, (base_move,500))
	screen.blit(base, (base_move + 500,500))

def create_pipe(pos):
	pipe_rect = pipe_surface.get_rect(midtop = (500,pos))
	return pipe_rect

def create_r_pipe(pos):
	pipe_r_rect = pipe_rotate.get_rect(midtop = (500,pos-550))
	return pipe_r_rect


def move_pipe(pipes,stop):
	if not(stop):
		for pipe in pipes:
			pipe.centerx -= 2
	return pipes

def draw_pipe(pipes):
	for pipe in pipes:
		screen.blit(pipe_surface, pipe)

def draw_r_pipe(pipes):
	for pipe in pipes:
		screen.blit(pipe_rotate, pipe)

pygame.init()

screen = pygame.display.set_mode((500,600))
clock = pygame.time.Clock()

bg = pygame.image.load('sprites/background-night.png').convert()
bg = pygame.transform.scale(bg, (500,600))

base_move = 0

base = pygame.image.load('sprites/base.png').convert()
base = pygame.transform.scale(base, (500,100))

gravity = 0.25
bird_move = 0
bird = pygame.image.load('sprites/bluebird-upflap.png').convert()
bird = pygame.transform.scale(bird, (50,40))
bird_rect = bird.get_rect(center = (100,250))

pipe_surface = pygame.image.load('sprites/pipe-green.png').convert()
pipe_surface = pygame.transform.scale(pipe_surface, (70,400))
pipe_rotate = pygame.transform.rotate(pipe_surface, 180)

pipe_list = []
pipe_r_list = []
SPAWNPIPE = pygame.USEREVENT
pipe_height = [200,225,250,275,300,325,350,375,400]

stop = False
count = 0
score = 0

message = pygame.image.load('sprites/message.png').convert()
message = pygame.transform.scale(message, (500,900))

gameover = pygame.image.load('sprites/gameover.png').convert()
gameover = pygame.transform.scale2x(gameover)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				if not(stop):
					count += 1
					bird_move = 0
					bird_move -= 4
					bird = pygame.image.load('sprites/bluebird-downflap.png').convert()
					bird = pygame.transform.scale(bird, (50,40))
					bird = pygame.transform.rotate(bird, 30)
					bird_rect = bird.get_rect(center = (100,bird_rect.centery))

		if event.type == SPAWNPIPE:
			pos = random.choice(pipe_height)
			pipe_list.append(create_pipe(pos))
			pipe_r_list.append(create_r_pipe(pos))


	if count > 0:
		screen.blit(bg, (0,0))

	pipe_list = move_pipe(pipe_list,stop)
	pipe_r_list = move_pipe(pipe_r_list,stop)
	draw_pipe(pipe_list)
	draw_r_pipe(pipe_r_list)

	base_move -= 2
	base_movement()

	if base_move <= -500:
		base_move = 0



	if bird_move >= 1 and bird_move < 2:
		bird = pygame.image.load('sprites/bluebird-midflap.png').convert()
		bird = pygame.transform.scale(bird, (50,40))
		bird = pygame.transform.rotate(bird,30)
		bird_rect = bird.get_rect(center = (100, bird_rect.centery))

	if bird_move >= 2 and bird_move < 3:
		bird = pygame.image.load('sprites/bluebird-midflap.png').convert()
		bird = pygame.transform.scale(bird, (50,40))
		bird = pygame.transform.rotate(bird,15)
		bird_rect = bird.get_rect(center = (100, bird_rect.centery))

	if bird_move >= 3 and bird_move < 4:
		bird = pygame.image.load('sprites/bluebird-midflap.png').convert()
		bird = pygame.transform.scale(bird, (50,40))
		bird = pygame.transform.rotate(bird,0)
		bird_rect = bird.get_rect(center = (100, bird_rect.centery))

	if bird_move >= 4 and bird_move < 5:
		bird = pygame.image.load('sprites/bluebird-upflap.png').convert()
		bird = pygame.transform.scale(bird, (50,40))
		bird = pygame.transform.rotate(bird,-15)
		bird_rect = bird.get_rect(center = (100, bird_rect.centery))

	if bird_move >= 5 and bird_move < 6:
		bird = pygame.image.load('sprites/bluebird-upflap.png').convert()
		bird = pygame.transform.scale(bird, (50,40))
		bird = pygame.transform.rotate(bird,-30)
		bird_rect = bird.get_rect(center = (100, bird_rect.centery))
	
	if bird_move >= 6:
		bird = pygame.image.load('sprites/bluebird-upflap.png').convert()
		bird = pygame.transform.scale(bird, (50,40))
		bird = pygame.transform.rotate(bird,-45)
		bird_rect = bird.get_rect(center = (100, bird_rect.centery))

	if bird_move < 6 and count >= 1:
		bird_move += ((gravity ** 2) * 3)

	if count == 1:
		pygame.time.set_timer(SPAWNPIPE, 1200)



	if bird_rect.centery >= 480:
		bird_move = 0
		stop = True

	for pipe in pipe_list:
		if bird_rect.colliderect(pipe):
			stop = True

	for pipe in pipe_r_list:
		if bird_rect.colliderect(pipe):
			stop = True


	bird_rect.centery += bird_move
	screen.blit(bird, bird_rect)

	if count == 0:
		screen.blit(message, (0,-200))

	if stop and count > 0:
		pygame.time.set_timer(SPAWNPIPE, 0)
		gravity = 0.5
		base_move = 0
		screen.blit(gameover, (60,200))

	clock.tick(120)
	pygame.display.update()