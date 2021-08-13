import pygame, random
from math import sqrt, pi

pygame.init();

#global values

display_width = 1920
display_height = 1030
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('PokeTower-Attack and Defend')
font = pygame.font.Font('freesansbold.ttf', display_height//28)

#defining colors

coffee_brown =((200,190,140))
forest_green = ((0,50,0))
navy_blue = ((0,0,100))
white = ((255,255,255))
blue = ((0,0,255))
green = ((0,255,0))
red = ((255,0,0))
black = ((0,0,0))
orange = ((255,100,10))
yellow = ((255,255,0))
blue_green = ((0,255,170))
marroon = ((115,0,0))
lime = ((180,255,100))
pink = ((255,100,180))
purple = ((240,0,255))
gray = ((127,127,127))
magenta = ((255,0,230))
brown = ((100,40,0))
silver = ((192, 192, 192))
gold = ((255, 215, 0))

transparent = pygame.Surface((display_width, display_height))
transparent.set_alpha(168)

#Functions

def dist(a, b):
	return sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def textbox(x, y, l, b, text, events, active):
	font = pygame.font.Font(None, b)
	input_box = pygame.Rect(x, y, l, b)
	colors = [gold, orange]
	color = colors[active]


	for event in events:
		if event.type == pygame.MOUSEBUTTONDOWN:
			if input_box.collidepoint(event.pos):
				active = True
			else:
				active = False
		if event.type == pygame.KEYDOWN:
			if active:
				if event.key == pygame.K_RETURN:
					active = False
				elif event.key == pygame.K_BACKSPACE:
					text = text[:-1]
				else:
					text += event.unicode

	txt_surface = font.render(text, True, color)
	width = max(l, txt_surface.get_width()+10)
	input_box.w = width
	gameDisplay.blit(txt_surface, (input_box.x+5, input_box.y+5))
	pygame.draw.rect(gameDisplay, color, input_box, 2)

	return text, active

def loadimage(path, l, h):
	m = pygame.image.load(path)
	m = pygame.transform.scale(m, (l, h))

	return m

def loadsound(path):
	if path == None:
		return None

	return pygame.mixer.Sound(path)

def colpatch(color, l, b, transparency, x, y):
	trans = pygame.Surface((l, b))
	trans.set_alpha(transparency)
	trans.fill(color)

	gameDisplay.blit(trans, (x, y))

	return trans

def boxed(img, x, y, l, b):
	mouse = pygame.mouse.get_pos()

	box = loadimage('Images/square.png', l, b)

	image(img, x, y)

	if mouse[0] >= x and mouse[0] <= x + l and mouse[1] >= y and mouse[1] <= y + b:
		image(box, x, y)

def message(msg, color, a, b):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [a, b])
	
def writes(msg, color, a, b, size):
    Fonts = pygame.font.Font('freesansbold.ttf', size)
    screen_text = Fonts.render(msg, True, color)
    gameDisplay.blit(screen_text, [a, b])

def Button(text, p1, p2, textcolor1, textcolor2, x, y, l, b, color1, color2):
    mouse = pygame.mouse.get_pos()
	
    if x < mouse[0] < x + l and y < mouse[1] < y + b:
	    pygame.draw.rect(gameDisplay, color2, [x, y, l, b])
	    message(text, textcolor2, p1, p2)
		
    else:
	    pygame.draw.rect(gameDisplay, color1, [x, y, l, b])
	    message(text, textcolor1, p1, p2)

def inmouse(x, y, l, b):
	mouse = pygame.mouse.get_pos()

	if x <= mouse[0] <= x + l and y <= mouse[1] <= y + b:
		return True

	return False

def image(image, a, b):
    gameDisplay.blit(image, (a, b))

def siimage(image, a, b, sizex, sizey):
	img = pygame.transform.scale(image, (sizex, sizey))
	gameDisplay.blit(img, (a, b))

def sound(sound):
    if sound == None:
	    return 1

    pygame.mixer.Sound.play(sound)
	
def sound1(sound):
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.Sound.play(sound)
    pygame.mixer.music.set_volume(1.0)
	
def number(m, n):
	x = int(round(random.randrange(m, n)/1.0) * 1.0)
		
	return x