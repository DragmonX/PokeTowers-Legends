from propervalues import *
from Data import *
from Tower import *
from Mapmaker import *
import pygame, time, random

pygame.init()

#hard coding

tilesize = display_width//20
buttonsize = display_height//12
placesizex, placesizey = display_width//20, display_height//10
arrowsize = display_height//30
fencesize = display_width//20
fram = 10

# importing images

ppbackground = loadimage('Images/ppbackground.jpg', display_width, display_height)
fpbackground1 = loadimage('Images/fpbackground1.jpg', display_width, display_height)
fpbackground2 = loadimage('Images/fpbackground2.jpg', display_width, display_height)
gametext = loadimage('Images/gametext.png', display_width//2, display_height//4)
darrow = loadimage('Images/downarrow.png', arrowsize, arrowsize)
uarrow = loadimage('Images/uparrow.png', arrowsize, arrowsize)
rarrow = loadimage('Images/rightarrow.png', display_width//30, display_height//6 + display_height//10)
offline = loadimage('Images/offline.png', display_width//12, display_width//12)
gbutton = loadimage('Images/goldbutton.png', display_width//12, display_width//12)
ptower = loadimage('Images/printtower.png', display_width//18, display_width//18)
playbutton = loadimage('Images/play.png', display_width//28, display_width//28)
mapbutton = loadimage('Images/map.png', display_width//32, display_width//32)
playmap = loadimage('Images/playmap.png', display_width//18, display_width//18)

#game coding

clock = pygame.time.Clock()

def playerpage():
	quit = False
	mselect = 0

	mtrans = [170, 140, 140, 140]
	tbactive = False

	loadmap = False
	loadse, scr = 0, 0

	while not quit:
		events = pygame.event.get()
		mouse = pygame.mouse.get_pos()
		for event in events:
			if event.type == pygame.QUIT:
				quit = True

		image(ppbackground, 0, 0)

		tx, ty = 0, display_height//6

		pygame.draw.rect(gameDisplay, white, [tx, ty - 1, display_width//9, 1])

		for i in range(4):
			for event in events:
				if event.type == pygame.MOUSEBUTTONDOWN and not loadmap:
					if inmouse(tx, ty, display_width//9, display_height//6):
						mtrans[mselect] = 140
						mselect = i
						mtrans[mselect] = 170


			colpatch(gold, display_width//9, display_height//6, mtrans[i], tx, ty)
			pygame.draw.rect(gameDisplay, white, [tx, ty + display_height//6, display_width//9, 1])

			if mselect == i:
				image(rarrow, tx + display_width//9 - display_width//95, ty - display_height//20)

			ty += display_height//6 + 1

		image(offline, display_width//18 - display_width//24, display_height//6 + display_height//12 - display_width//24)

		if mselect == 0:
			image(gbutton, display_width//2 - display_width//4, display_height//2 - display_height//3)
			image(ptower, display_width//2 - display_width//4 + display_width/76, display_height//2 - display_height//3 + display_height//50)

			image(gbutton, display_width//2, display_height//2 - display_height//6)
			siimage(playmap, display_width//2+display_width//55, display_height//2 - display_height//6 + display_height//33, display_width//23, display_width//23)

			for event in events:
				if event.type == pygame.MOUSEBUTTONDOWN and not loadmap:
					if inmouse(display_width//2 - display_width//4, display_height//2 - display_height//4, display_width//12, display_width//12):
						tiles, partow = randscreen()
						p = maingam(0, tiles, partow)

						if not p:
							quit = True
						else:
							return 1

					elif inmouse(display_width//2+display_width//55, display_height//2 - display_height//6 + display_height//33, display_width//23, display_width//23):
						loadmap = True

		if loadmap:
			colpatch(black, display_width, display_height, 130, 0, 0)

			textsize = display_height//28
			
			Button("Load", 3*display_width//8, 3*display_height//4, white, white, display_width//4, 3*display_height//4-display_height//32, display_width//4, display_height//16+textsize, black, white, 0, 50, textsize)
			Button("Cancel", 5*display_width//8, 3*display_height//4, white, white, display_width//2, 3*display_height//4-display_height//32, display_width//4, display_height//16+textsize, black, white, 0, 50, textsize)

			image(load, 5*display_width//16-display_height//100, 3*display_height//4)
			image(cross, 9*display_width//16 - display_height//100, 3*display_height//4-display_height//200)

			for event in events:
				if event.type == pygame.MOUSEBUTTONDOWN:
					if inmouse(display_width//2, 3*display_height//4-display_height//32, display_width//4, display_height//16+textsize):
						loadmap = False
						loadse = 0
					elif inmouse(display_width//4, 3*display_height//4-display_height//32, display_width//4, display_height//16+textsize) and loadse:
						data = dat[1][loadse - 1]

						p = maingam(0, data[0], data[1])

						if not p:
							quit = True
						else:
							return 1

						loadse = 0

			colpatch(white, display_width//2, display_height//2 - display_height//32, 80, display_width//4, display_height//4)

			for i in range(scr, min(len(dat[1]), 9)):
				filname = dat[1][i][3]

				if loadse == i+1:
					Button(filname, (i%2+1)*display_width//4, ((i-scr)//2)*textsize+display_height//4, white, white, (i%2+1)*display_width//4, ((i-scr)//2)*textsize+display_height//4, display_width//4, textsize, white, black, 0, 0, textsize)
				else:
					Button(filname, (i%2+1)*display_width//4, ((i-scr)//2)*textsize+display_height//4, black, black, (i%2+1)*display_width//4, ((i-scr)//2)*textsize+display_height//4, display_width//4, textsize, white, black, 0, 50, textsize)

				for event in events:
					if event.type == pygame.MOUSEBUTTONDOWN:
						if inmouse((i%2+1)*display_width//4, ((i-scr)//2)*textsize+display_height//4, display_width//4, textsize):
							loadse = i+1



		
		dat[0], tbactive = textbox(display_width//100, display_height//100, display_width//8, display_height//25, dat[0], events, tbactive)
				
		
		pygame.display.update()

	return 0


def firstpage():
	quit = False

	pygame.mixer.music.load('Sound/Theme.wav')
	pygame.mixer.music.play(-1)
	

	while not quit:
		events = pygame.event.get()
		mouse = pygame.mouse.get_pos()
		for event in events:
			if event.type == pygame.QUIT:
				quit = True

		image(fpbackground1, 0, 0)

		image(gametext, display_width//4, display_height//19)

		colpatch(white, display_width//8, display_height, 90, display_width//10, 0)

		Button("Play", display_width//8 + display_width//30, display_height//3, black, black, display_width//10, display_height//3 - display_height//50, display_width//8, display_height//13, white, black, 0, 50)
		image(playbutton, display_width//8-display_width//40, display_height//3-display_height//60)

		Button("Editor", display_width//8 + display_width//30, display_height//3 + display_height//13, black, black, display_width//10, display_height//3 - display_height//50 + display_height//13, display_width//8, display_height//13, white, black, 0, 50)
		image(mapbutton, display_width//8-display_width//50, display_height//3-display_height//100 + display_height//13)


		for event in events:
			if event.type == pygame.MOUSEBUTTONDOWN:
				if inmouse(display_width//10, display_height//3 - display_height//50, display_width//8, display_height//13):
					p = playerpage()
					if not p:
						quit = True
					else:
						continue

				if inmouse(display_width//10, display_height//3 - display_height//50 + display_height//13, display_width//8, display_height//13):
					p = Map([[], [], 'background', "", False])
					if not p:
						quit = True
					else:
						continue

		pygame.display.update()

firstpage()
wplayerdata("PlayerData.dat", dat)