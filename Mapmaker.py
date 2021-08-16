from propervalues import *
from Data import *

pygame.init()

#hardcoding

tilesize = display_width//20

#importing images

tile = loadimage('Images/tile.jpeg', tilesize, tilesize)
tools = loadimage('Images/tools.png', display_width//30, display_width//30)
more = loadimage('Images/more.png', display_width//32, display_width//32)

#File Coding

def Map(data):
	#data -> [tiles, tow, back]

	quit = False

	toolse = 0
	tool = 0

	while not quit:
		events = pygame.event.get()
		mouse = pygame.mouse.get_pos()
		for event in events:
			if event.type == pygame.QUIT:
				quit = True

		image(data[2], 0, 0)

		Button("", 0, 0, black, black, 0, 0, display_width//30, display_width//30, black, black, 0, 90)
		image(tools, 0, 0)

		Button("", 0, 0, black, black, display_width//30, 0, display_width//30, display_width//30, black, black, 0, 90)
		image(more, display_width//30+(display_width//30 - display_width//32)//2, 0)



		if toolse == 1:
			n = 1+len(tower)
			l = int(sqrt(n-1)+1)

			Button("", 0, 0, black, black, display_width//30, display_width//30, l*display_width//30, (n+2)//l * display_width//30, black, black, 90, 90)
			Button("", 0, 0, black, black, display_width//30, display_width//30, display_width//30, display_width//30, black, white, 0, 50)
			siimage(tile, display_width//30+display_width//120, display_width//30+display_width//120, display_width//30-display_width//60, display_width//30-display_width//60)

			x, y, i = display_width//15, display_width//30, 2

			for tow in tower:
				Button("", 0, 0, black, black, x, y, display_width//30, display_width//30, black, white, 0, 50)
				siimage(tow.img, x, y, display_width//30, display_width//30)
				
				if i % l:
					x += display_width//30
				else:
					x = display_width//30
					y += display_width//30

				i += 1

			for event in events:
				if event.type == pygame.MOUSEBUTTONDOWN:
					for j in range(n):
						if inmouse(display_width//30*(j%l+1), display_width//30*(j//l+1), display_width//30, display_width//30):
							tool = j+1

		if tool:
			if tool == 1:
				image(tile, mouse[0]-tilesize//2, mouse[1]-tilesize//2)
			elif  tool <= len(tower)+1:
				image(tower[tool-2].img, mouse[0]-tower[tool-2].l//2, mouse[1]-tower[tool-2].b//2)

			for event in events:
				if event.type == pygame.MOUSEBUTTONDOWN:
					if event.button == 3:
						tool = 0


		for event in events:
			if event.type == pygame.MOUSEBUTTONDOWN:
				if inmouse(0, 0, display_width//30, display_width//30) and toolse != 1:
					toolse = 1
				elif inmouse(display_width//30, 0, display_width//30, display_width//30):
					toolse = 2
				elif toolse == 1:
					toolse = 0

		pygame.display.update()

