from propervalues import *
from Data import *

pygame.init()

#hardcoding

tilesize = display_width//20

#importing images

tile = loadimage('Images/tile.jpeg', tilesize, tilesize)
tools = loadimage('Images/tools.png', display_width//30, display_width//30)
more = loadimage('Images/more.png', display_width//32, display_width//32)
home = loadimage('Images/home.png', display_height//28, display_height//28)
save = loadimage('Images/save.png', display_height//28, display_height//28)
saveas = loadimage('Images/saveas.png', display_height//28, display_height//28)


#File Coding

def Map(data):
	#data -> [tiles, tow, back]

	quit = False

	toolse = 0
	tool, opti = 0, 0

	positions = []

	for i in range((display_width//tilesize + 1) * (display_height//tilesize)):
		positions.append(0)

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

		for til in data[0]:
			image(tile, til[0], til[1])

		for to in data[1]:
			image(tower[to[2]].img, to[0], to[1])

		if tool:
			if tool == 1:
				image(tile, mouse[0]-tilesize//2, mouse[1]-tilesize//2)
			elif  tool <= len(tower)+1:
				image(tower[tool-2].img, mouse[0]-tower[tool-2].l//2, mouse[1]-tower[tool-2].b//2)

			currpos = [mouse[0]//tilesize, (display_height - mouse[1])//tilesize]

			tileno = currpos[0]*(display_height//tilesize) + currpos[1]

			if currpos[1] < display_height//tilesize:
				colpatch(black, tilesize, tilesize, 50, currpos[0]*tilesize, display_height - (currpos[1]+1)*tilesize)

			for event in events:
				if event.type == pygame.MOUSEBUTTONDOWN:
					if event.button == 3:
						tool = 0
					elif event.button == 1:
						if tool == 1 and currpos[1] < display_height//tilesize and positions[tileno] == 0:
							data[0].append((currpos[0]*tilesize, display_height - (currpos[1]+1)*tilesize, tileno))
							positions[tileno] = 1
						elif 1 < tool <= 1 + len(tower) and currpos[1] < display_height//tilesize and positions[tileno] == 0:
							data[1].append((currpos[0]*tilesize, display_height - (currpos[1]+1)*tilesize, tool - 2, tileno))
							positions[tileno] = tool


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
				if event.type == pygame.MOUSEBUTTONDOWN:
					for j in range(n):
						if inmouse(display_width//30*(j%l+1), display_width//30*(j//l+1), display_width//30, display_width//30):
							tool = j+1

		elif toolse == 2:
			colpatch(black, display_width, display_height, 130, 0, 0)

			textsize = display_height//28

			Button("Home", 3*display_width//8, display_height//4, white, white, display_width//4, display_height//4-display_height//32, display_width//4, display_height//16+textsize, black, white, 0, 50, textsize)
			Button("SaveAs", 3*display_width//8, display_height//4+textsize+display_height//16, white, white, display_width//4, display_height//4+textsize+display_height//16-display_height//32, display_width//4, display_height//16+textsize, black, white, 0, 50, textsize)
			Button("Save", 3*display_width//8, display_height//4+2*textsize+2*display_height//16, white, white, display_width//4, display_height//4+2*textsize+2*display_height//16-display_height//32, display_width//4, display_height//16+textsize, black, white, 0, 50, textsize)

			image(home, 5*display_width//16-display_height//80, display_height//4)
			image(saveas, 5*display_width//16-display_height//100, display_height//4+textsize+display_height//16)
			image(save, 5*display_width//16-display_height//100, display_height//4+2*textsize+2*display_height//16)

			for event in events:
				if event.type == pygame.MOUSEBUTTONDOWN:
					k = 0
					for i in range(3):
						if inmouse(((i//4)+1)*display_width//4, display_height//4+(i%4)*(textsize+display_height//16)-display_height//32, display_width//4, display_height//16+textsize):
							opti = i+1
							k = 1
					if not k:
						toolse = 0

			if opti == 1:
				quit = True
				return 1

		for event in events:
			if event.type == pygame.MOUSEBUTTONDOWN:
				if inmouse(0, 0, display_width//30, display_width//30) and toolse == 0:
					toolse = 1
					tool = 0
				elif inmouse(display_width//30, 0, display_width//30, display_width//30):
					toolse = 2
					tool = 0
				elif toolse == 1:
					toolse = 0






		pygame.display.update()