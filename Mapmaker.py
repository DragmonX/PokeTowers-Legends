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
cross = loadimage('Images/cross.png', display_height//28, display_height//28)
load = loadimage('Images/load.png', display_height//28, display_height//28)

#File Coding

def Map(data):
	#data -> [tiles, tow, back]

	quit = False

	toolse = 0
	tool, opti = 0, 0
	fname = data[3]

	background = loadimage('Images/%s.jpg'%data[2], display_width, display_height)

	savetb = 0

	loadse, scr = 0, 0

	positions = []

	for i in range((display_width//tilesize + 1) * (display_height//tilesize)):
		positions.append(0)

	while not quit:
		events = pygame.event.get()
		mouse = pygame.mouse.get_pos()
		for event in events:
			if event.type == pygame.QUIT:
				quit = True

		if not tool and not toolse:
			for event in events:
				if event.type == pygame.MOUSEBUTTONDOWN:
					if event.button == 3:
						currpos = [mouse[0]//tilesize, (display_height - mouse[1])//tilesize]
						tileno = currpos[0]*(display_height//tilesize) + currpos[1]

						if positions[tileno] == 1:
							for til in range(len(data[0])):
								if data[0][til][2] == tileno:
									for p in range(til, len(data[0])):
										positions[data[0][p][2]] = 0
									del data[0][til:]
									break
						elif 1 <= positions[tileno] <= 1+len(tower):
							for til in data[1]:
								if til[3] == tileno:
									data[1].remove(til)
									positions[tileno] = 0
									break




		image(background, 0, 0)

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

				if event.type == pygame.MOUSEBUTTONDOWN:
					for j in range(n):
						if inmouse(display_width//30*(j%l+1), display_width//30*(j//l+1), display_width//30, display_width//30):
							tool = j+1

				i+=1

		elif toolse == 2:
			if opti == 0:
				colpatch(black, display_width, display_height, 130, 0, 0)

				textsize = display_height//28

				Button("Home", 3*display_width//8, display_height//4, white, white, display_width//4, display_height//4-display_height//32, display_width//4, display_height//16+textsize, black, white, 0, 50, textsize)
				Button("SaveAs", 3*display_width//8, display_height//4+textsize+display_height//16, white, white, display_width//4, display_height//4+textsize+display_height//16-display_height//32, display_width//4, display_height//16+textsize, black, white, 0, 50, textsize)
				Button("Save", 3*display_width//8, display_height//4+2*textsize+2*display_height//16, white, white, display_width//4, display_height//4+2*textsize+2*display_height//16-display_height//32, display_width//4, display_height//16+textsize, black, white, 0, 50, textsize)
				Button("Load", 3*display_width//8, display_height//4+3*textsize+3*display_height//16, white, white, display_width//4, display_height//4+3*textsize+3*display_height//16-display_height//32, display_width//4, display_height//16+textsize, black, white, 0, 50, textsize)

				image(home, 5*display_width//16-display_height//80, display_height//4)
				image(saveas, 5*display_width//16-display_height//100, display_height//4+textsize+display_height//16)
				image(save, 5*display_width//16-display_height//100, display_height//4+2*textsize+2*display_height//16)
				image(load, 5*display_width//16-display_height//100, display_height//4+3*textsize+3*display_height//16)

				for event in events:
					if event.type == pygame.MOUSEBUTTONDOWN:
						k = 0
						for i in range(4):
							if inmouse(((i//4)+1)*display_width//4, display_height//4+(i%4)*(textsize+display_height//16)-display_height//32, display_width//4, display_height//16+textsize):
								opti = i+1
								k = 1
						if not k:
							toolse = 0

			elif opti == 1:
				quit = True
				return 1
			elif opti == 2:
				colpatch(black, display_width, display_height, 130, 0, 0)

				textsize = display_height//28

				Button("Save", 3*display_width//8, 3*display_height//4, white, white, display_width//4, 3*display_height//4-display_height//32, display_width//4, display_height//16+textsize, black, white, 0, 50, textsize)
				Button("Cancel", 5*display_width//8, 3*display_height//4, white, white, display_width//2, 3*display_height//4-display_height//32, display_width//4, display_height//16+textsize, black, white, 0, 50, textsize)

				image(save, 5*display_width//16-display_height//100, 3*display_height//4)
				image(cross, 9*display_width//16 - display_height//100, 3*display_height//4-display_height//200)

				for event in events:
					if event.type == pygame.MOUSEBUTTONDOWN:
						if inmouse(display_width//2, 3*display_height//4-display_height//32, display_width//4, display_height//16+textsize):
							opti = 0
							data[3] = fname
						elif inmouse(display_width//4, 3*display_height//4-display_height//32, display_width//4, display_height//16+textsize):
							dat[1].append(data)
							fname = data[3]
							opti = 0
							toolse = 0

				data[3], savetb = textbox(display_width//4, 3*display_height//4-display_height//32-textsize, display_width//2, textsize, data[3], events, savetb, gray, white)

			elif opti == 3:
				found = False
				for d in range(len(dat[1])):
					if dat[1][d][3] == fname:
						dat[1][d] = data
						found  = True
						opti = 0
						toolse = 0
				if not found:
					opti = 2

			elif opti == 4:
				colpatch(black, display_width, display_height, 130, 0, 0)

				textsize = display_height//28
				
				Button("Load", 3*display_width//8, 3*display_height//4, white, white, display_width//4, 3*display_height//4-display_height//32, display_width//4, display_height//16+textsize, black, white, 0, 50, textsize)
				Button("Cancel", 5*display_width//8, 3*display_height//4, white, white, display_width//2, 3*display_height//4-display_height//32, display_width//4, display_height//16+textsize, black, white, 0, 50, textsize)

				image(load, 5*display_width//16-display_height//100, 3*display_height//4)
				image(cross, 9*display_width//16 - display_height//100, 3*display_height//4-display_height//200)

				for event in events:
					if event.type == pygame.MOUSEBUTTONDOWN:
						if inmouse(display_width//2, 3*display_height//4-display_height//32, display_width//4, display_height//16+textsize):
							opti = 0
							data[3] = fname
							loadse = 0
						elif inmouse(display_width//4, 3*display_height//4-display_height//32, display_width//4, display_height//16+textsize) and loadse:
							data = dat[1][loadse - 1]
							fname = data[3]
							opti = 0
							toolse = 0
							loadse = 0

							for p in range(len(positions)):
								positions[p] = 0

							for d in data[0]:
								positions[d[2]] = 1
							for d in data[1]:
								positions[d[3]] = d[2] + 2


				colpatch(white, display_width//2, display_height//2 - display_height//32, 30, display_width//4, display_height//4)

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





			else:
				opti = 0
				toolse = 0



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