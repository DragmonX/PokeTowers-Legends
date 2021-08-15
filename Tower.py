from propervalues import *
from Data import *
from math import atan, pi, sin, cos
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

background = loadimage('Images/background.jpg', display_width, display_height)
background2 = loadimage('Images/background2.jpg', display_width, display_height)
tile = loadimage('Images/tile.jpeg', tilesize, tilesize)
button = loadimage('Images/button2dhover.png', buttonsize, buttonsize)
buttonp = loadimage('Images/button2dpressed.png', buttonsize, buttonsize)
darrow = loadimage('Images/downarrow.png', arrowsize, arrowsize)
uarrow = loadimage('Images/uparrow.png', arrowsize, arrowsize)
fence = loadimage('Images/fence.png', fencesize, fencesize)
rancircle = loadimage('Images/RanCircle.png', 501, 501)
coin = loadimage('Images/coin.png', display_width//60, display_width//60)
heart = loadimage('Images/heart.png', display_width//60, display_width//60)
shield = loadimage('Images/shield.png', display_width//60, display_width//60)
speed = loadimage('Images/speed.png', display_width//60, display_width//60)
sword = loadimage('Images/sword.png', display_width//60, display_width//60)

#game coding

tiles = []
towers = [] # [x, y, type]

clock = pygame.time.Clock()


def randscreen():
	y = display_height - tilesize
	x = 0

	tiles.append((x, y))

	x += tilesize
	tiles.append((x, y))

	while x < display_width - tilesize:
		nt =  number(1, 100)

		if nt < 70:
			x += tilesize
		elif y >= tilesize:
			y -= tilesize

		tiles.append((x, y))

	x += tilesize
	tiles.append((x, y))

	i = 1

	while i < len(tiles) - 2:
		a = tiles[i]
		pl = number(1, 101)
		xc = a[0]
		yc = a[1]

		if pl <= 30:
			if tiles[i - 1][0] == a[0] and a[0] - tower[0].l >= 0:
				xc = a[0] - tower[0].l
				towers.append([xc, yc, 0])
				i+=1
			elif tiles[i - 1][1] == a[1] and a[1] - tower[0].b >= 0:
				yc = a[1] - tower[0].b
				towers.append([xc, yc, 0])
				i+=1


		elif pl <= 60:
			if tiles[i + 1][1] == a[1] and a[1] + tilesize <= display_height - tower[0].b:
				yc = a[1] + tilesize
				towers.append([xc, yc, 0])
				i+=1
			elif tiles[i + 1][0] == a[0] and a[0] + tilesize <= display_width - tower[0].l:
				xc = a[0] + tilesize
				towers.append([xc, yc, 0])
				i+=1

		elif pl <= 85:
			if tiles[i + 1][1] == a[1] and a[1] + tilesize <= display_height - tower[0].b:
				yc = a[1] + tilesize
				towers.append([xc, yc, 0])
			elif tiles[i + 1][0] == a[0] and a[0] + tilesize <= display_width - tower[0].l:
				xc = a[0] + tilesize
				towers.append([xc, yc, 0])

			if tiles[i - 1][0] == a[0] and a[0] - tower[0].l >= 0:
				xc = a[0] - tower[0].l
				towers.append([xc, yc, 0])
			elif tiles[i - 1][1] == a[1] and a[1] - tower[0].b >= 0:
				yc = a[1] - tower[0].b
				towers.append([xc, yc, 0])


			i += 1

		i += 1

	for a in tiles:
		for b in towers:
			if a[0] == b[0] and a[1] == b[1]:
				towers.remove(b)

	i = 0

	for a in towers:
		for j in range(i):
			if a == towers[j]:
				towers.pop(j)
		i+=1

def findir(ele):
	for i in range(len(tiles) - 1):
		if tiles[i][0] <= ele[0] - (tilesize//2 - 16) <= tiles[i][0] + tilesize and tiles[i][1] <= ele[1] + tilesize//2 + 16 <= tiles[i][1] + tilesize:
			if tiles[i][0] == tiles[i + 1][0] and tiles[i][1] < tiles[i + 1][1]:
				return 3
			elif tiles[i][0] == tiles[i + 1][0] and tiles[i][1] > tiles[i + 1][1]:
				return 1
			elif tiles[i][0] < tiles[i + 1][0] and tiles[i][1] == tiles[i + 1][1]:
				return 2
			elif tiles[i][0] > tiles[i + 1][0] and tiles[i][1] == tiles[i + 1][1]:
				return 4

	return 2


def maingam(tot):
	randscreen()

	#song

	pygame.mixer.music.load('Sound/Battle.wav')
	pygame.mixer.music.play(-1)

#________________________________________________________________________________________________________________________________

	#variables

	toselected = [0, 0, 0]
	quit = False
	troops = [] #[[troop index, troop number]]
	nextl = 0
	
	#main-loop

	while not quit:
		mouse = pygame.mouse.get_pos()
		events = pygame.event.get()
		for event in events:
		    if event.type == pygame.QUIT:
			    quit = True

		image(background, 0, 0)

		
		for a in tiles:
			image(tile, a[0], a[1])

		for a in towers:
			tower[a[2]].dis(a[0], a[1])

			if inmouse(a[0], a[1], tower[a[2]].l, tower[a[2]].b):
				siimage(rancircle, a[0]+tower[a[2]].l//2-tower[a[2]].rang, a[1]+tower[a[2]].b//2-tower[a[2]].rang, 2*tower[a[2]].rang, 2*tower[a[2]].rang)
			
			if a[2] == 1:
				image(sprite[1].get_image(13), a[0] + tower[a[2]].l//4, a[1]-sprite[1].height+17)

		if nextl == 0:
			maketower = False
			for a in towers:
				if toselected == a:
					pygame.draw.rect(gameDisplay, blue, [a[0]+tower[co[2]].l, a[1]-tower[co[2]].b, tower[co[2]].l * len(tower), tower[co[2]].b])
					x, y = a[0]+tower[co[2]].l, a[1]-tower[co[2]].b
					for i in range(0, len(tower)):
						if i == a[2]:
							continue

						tower[i].dis(x, y)

						if inmouse(x, y, tower[i].l, tower[i].b):
							siimage(rancircle, a[0]+tower[i].l//2-tower[i].rang, a[1]+tower[i].b//2-tower[i].rang, 2*tower[i].rang, 2*tower[i].rang)

						x += tower[i].l + 2

					x, y = a[0]+tower[co[2]].l, a[1]-tower[co[2]].b

					for i in range(0, len(tower)):
						if i == a[2]:
							continue
						for event in events:
							if event.type == pygame.MOUSEBUTTONDOWN:
								if inmouse(x, y, tower[co[2]].l, tower[co[2]].b):
									toselected = [0, 0, 0]
									a[2] = i
									maketower = True
									break

						x += tower[co[2]].l


			for event in events:
				if event.type == pygame.MOUSEBUTTONDOWN and not maketower:
					toselected = [0, 0, 0]

			for co in towers:
				for event in events:
					if event.type == pygame.MOUSEBUTTONDOWN:
					    if inmouse(co[0], co[1], tower[co[2]].l, tower[co[2]].b):
						    toselected = co

					break

		if nextl == 2:
			image(buttonp, display_height//70, display_width//124)
			break
		elif nextl == 0:
			image(button, display_height//70, display_width//124)
			for event in events:
				if event.type == pygame.MOUSEBUTTONDOWN:
					if display_height//70 <= mouse[0] <= display_height//70 + buttonsize and display_width//124 <= mouse[1] <= display_width//124 + buttonsize:
						nextl = 1
		else:
			transparent.fill(black)
			gameDisplay.blit(transparent, (0, 0))
			pygame.draw.rect(gameDisplay, brown, [display_width//4, display_height//3, display_width//2, display_height//3])
			writes("Are you sure to end your turn?", yellow, display_width//4 + display_width//12, display_height//3 + display_height//20, display_height//25)
			Button("Yes", display_width//4 + display_width//10 + display_width//55, display_height//3 + display_height//5 + display_height//70, black, white, display_width//4 + display_width//10, display_height//3 + display_height//5, display_width//14, display_height//16, white, black)
			Button("No", display_width - (display_width//4 + display_width//10 + display_width//14) + display_width//44, display_height//3 + display_height//5 + display_height//70, black, white, display_width - (display_width//4 + display_width//10 + display_width//14), display_height//3 + display_height//5, display_width//14, display_height//16, white, black)



			for event in events:
				if event.type == pygame.MOUSEBUTTONDOWN:
					if inmouse(display_width//4 + display_width//10, display_height//3 + display_height//5, display_width//14, display_height//16):
							nextl = 2
					elif inmouse(display_width - (display_width//4 + display_width//10 + display_width//14), display_height//3 + display_height//5, display_width//14, display_height//16):
							nextl = 0
		
		clock.tick(fram)

		pygame.display.update()

#________________________________________________________________________________________________________________________________

	imgt = 0
	st = 0
	trselected = 0
	mins = (display_height - 6 * (32 + 2 * display_height//20 + 1))//2
	nextl = 0

	while not quit:
		events = pygame.event.get()
		mouse = pygame.mouse.get_pos()
		for event in events:
			if event.type == pygame.QUIT:
				quit = True

		image(background2, 0, 0)
		pygame.draw.rect(gameDisplay, black, [display_width//20, 0, display_width - display_width//20, placesizey])
		pygame.draw.rect(gameDisplay, black, [0, 0, display_width//20, display_height])

		pygame.draw.rect(gameDisplay, white, [0, mins - 1, display_width//20, 2])

		for i in range(st, st + 6):
			Button("", 0, 0, white, white, 0, mins + (i - st) * 32 + 2 * (i - st) * display_height//20 + 1, display_width//20, 32 + 2 * display_height//20 - 2, black, gray)
			pokemon[i].move(3, imgt, display_width//40 - 16, mins + (i - st) * 32 + 2 * (i - st) * display_height//20 + display_height//20)
			pygame.draw.rect(gameDisplay, white, [0, mins + (i - st + 1) * 32 + 2 * (i - st + 1) * display_height//20 - 1, display_width//20, 2])
			for event in events:
				if event.type == pygame.MOUSEBUTTONDOWN:
					if inmouse(0, mins + (i - st) * 32 + 2 * (i - st) * display_height//20 + 1, display_width//20, 32 + 2 * display_height//20 - 2):
						trselected = i + 1

		if trselected:
			writes(pokemon[trselected-1].name, green, display_width//15, display_height//40, display_height//10-display_height//20)
			
			image(coin, display_width//15+display_width//5, display_height//40)
			writes("%s"%pokemon[trselected-1].cost, white, display_width//15+display_width//5.03, display_height//40+display_height//25, display_height//50)
			
			image(heart, display_width//15+display_width//5+display_width//15, display_height//40)
			writes("%s"%pokemon[trselected-1].hp, white, display_width//15+display_width//15+display_width//4.95, display_height//40+display_height//25, display_height//50)
			
			image(shield, display_width//15+display_width//5+2*display_width//15, display_height//40)
			if pokemon[trselected-1].defence<100:
				writes("%s"%pokemon[trselected-1].defence, white, display_width//15+2*display_width//15+display_width//4.95, display_height//40+display_height//25, display_height//50)
			else:
				writes("%s"%pokemon[trselected-1].defence, white, display_width//15+2*display_width//15+display_width//5.03, display_height//40+display_height//25, display_height//50)

			image(speed, display_width//15+display_width//5+3*display_width//15, display_height//40)
			if pokemon[trselected-1].speed<100:
				writes("%s"%pokemon[trselected-1].speed, white, display_width//15+3*display_width//15+display_width//4.95, display_height//40+display_height//25, display_height//50)
			else:
				writes("%s"%pokemon[trselected-1].speed, white, display_width//15+3*display_width//15+display_width//5.03, display_height//40+display_height//25, display_height//50)

			image(sword, display_width//15+display_width//5+4*display_width//15, display_height//40)
			if pokemon[trselected-1].attack<100:
				writes("%s"%pokemon[trselected-1].attack, white, display_width//15+4*display_width//15+display_width//4.95, display_height//40+display_height//25, display_height//50)
			else:
				writes("%s"%pokemon[trselected-1].attack, white, display_width//15+4*display_width//15+display_width//5.03, display_height//40+display_height//25, display_height//50)

		if nextl == 0 and trselected and mouse[0] > display_width//20 and mouse[0] < display_width - placesizex and mouse[1] > placesizey:
			for event in events:
				if event.type == pygame.MOUSEBUTTONDOWN:
					if event.button == 1:
						r = 10 - mouse[1]//placesizey
						c = (mouse[0]//placesizex)

						alre = False

						if c != 0:
							c = 19 - c

							for i in troops:
								if i[1] == 18 * (r - 1) + c:
									alre = True
									break

						if not alre:
							troops.append([trselected, 18 * (r - 1) + c])

					elif event.button == 3:
						r = 10 - mouse[1]//placesizey
						c = (mouse[0]//placesizex)

						ts = 0

						alre = False

						if c != 0:
							c = 19 - c

							for i in troops:
								if i[1] == 18 * (r - 1) + c:
									alre = True
									ts = i[0]
									break

						if alre:
							troops.remove([ts, 18 * (r - 1) + c])



			trans = pygame.Surface((placesizex, placesizey))
			trans.set_alpha(200)
			trans.fill(gray)

			gameDisplay.blit(trans, (mouse[0] - mouse[0] % placesizex, mouse[1] - mouse[1] % placesizey))
			pokemon[trselected - 1].move(3, 0, mouse[0] - 16, mouse[1] - 16)


		for troop in troops:
			pokemon[troop[0] - 1].move(2, 0, (19 - ((troop[1] - 1) % 18 + 1)) * placesizex + (placesizex - 32) // 2, display_height - (((troop[1] - 1) // 18) * placesizey + (placesizey - 32) // 2 + 32))
		
		if st > 0:
			Button("", 0, 0, black, black, 0, 0, display_width//20, mins - 1, gold, silver)
			image(uarrow, (display_width//20 - arrowsize)//2, (mins - 1 - arrowsize)//2)
			for event in events:
				if event.type == pygame.MOUSEBUTTONDOWN:
					if inmouse(0, 0, display_width//20, mins - 1):
						st -= 1
		else:
			Button("", 0, 0, black, black, 0, 0, display_width//20, mins - 1, gray, gray)
			image(uarrow, (display_width//20 - arrowsize)//2, (mins - 1 - arrowsize)//2)
		
		if st + 6 < len(pokemon):
			Button("", 0, 0, black, black, 0, mins + 12 * display_height//20 + 6 * 32 + 1, display_width//20, display_height - (mins + 12 * display_height//20 + 6 * 32 + 1), gold, silver)
			image(darrow, (display_width//20 - arrowsize)//2, mins + 12 * display_height//20 + 6 * 32 + 1 + (display_height - (mins + 12 * display_height//20 + 6 * 32 + 1) - arrowsize)//2)

			for event in events:
				if event.type == pygame.MOUSEBUTTONDOWN:
					if inmouse(0, mins + 12 * display_height//20 + 6 * 32 + 1, display_width//20, display_height - (mins + 12 * display_height//20 + 6 * 32 + 1)):
						st += 1
		else:
			Button("", 0, 0, black, black, 0, mins + 12 * display_height//20 + 6 * 32 + 1, display_width//20, display_height - (mins + 12 * display_height//20 + 6 * 32 + 1), gray, gray)
			image(darrow, (display_width//20 - arrowsize)//2, mins + 12 * display_height//20 + 6 * 32 + 1 + (display_height - (mins + 12 * display_height//20 + 6 * 32 + 1) - arrowsize)//2)


		if nextl == 2:
			image(buttonp, display_width - buttonsize - display_width//124, display_height//70)
			break
		elif nextl == 0:
			image(button, display_width - buttonsize - display_width//124, display_height//70)
			for event in events:
				if event.type == pygame.MOUSEBUTTONDOWN:
					if inmouse(display_width - buttonsize - display_width//124, display_height//70, buttonsize, buttonsize):
						nextl = 1
		else:
			transparent.fill(black)
			gameDisplay.blit(transparent, (0, 0))
			pygame.draw.rect(gameDisplay, brown, [display_width//4, display_height//3, display_width//2, display_height//3])
			writes("Are you sure to end your turn?", yellow, display_width//4 + display_width//12, display_height//3 + display_height//20, display_height//25)
			Button("Yes", display_width//4 + display_width//10 + display_width//55, display_height//3 + display_height//5 + display_height//70, black, white, display_width//4 + display_width//10, display_height//3 + display_height//5, display_width//14, display_height//16, white, black)
			Button("No", display_width - (display_width//4 + display_width//10 + display_width//14) + display_width//44, display_height//3 + display_height//5 + display_height//70, black, white, display_width - (display_width//4 + display_width//10 + display_width//14), display_height//3 + display_height//5, display_width//14, display_height//16, white, black)



			for event in events:
				if event.type == pygame.MOUSEBUTTONDOWN:
					if inmouse(display_width//4 + display_width//10, display_height//3 + display_height//5, display_width//14, display_height//16):
						nextl = 2
					elif inmouse(display_width - (display_width//4 + display_width//10 + display_width//14), display_height//3 + display_height//5, display_width//14, display_height//16):
						nextl = 0
				
		imgt = (imgt + 1) % 2

		pygame.display.update()

#________________________________________________________________________________________________________________________________

	nextl = 0
	trind = [] #[ind, x, y, hp, stats, ihp]
	tr, tim, samtro, timperwa = 1, 120, [], 120

	projectiles = []
	towtim = []
	crossed = 0

	print(troops)

	for i in range(len(towers)):
		towtim.append(0)

	for i in range(18):
		samtro.append(0)

	for i in range(len(troops)):
		iv = 50

		hpi = pokemon[troops[i][0] - 1].healthp(iv)
		sta = pokemon[troops[i][0] - 1].stats(iv)


		trind.append([0, -32, display_height - tilesize//2 - 16, hpi, sta, hpi])


	while not quit:
		mouse = pygame.mouse.get_pos()
		events = pygame.event.get()
		for event in events:
		    if event.type == pygame.QUIT:
			    quit = True

		image(background, 0, 0)

		
		for a in tiles:
			image(tile, a[0], a[1])

		for tow in range(len(towers)):
			a = towers[tow]
			tower[a[2]].dis(a[0], a[1])
			if a[2] == 1:
				image(sprite[1].get_image(towtim[tow]), a[0] + tower[a[2]].l//4, a[1]-sprite[1].height+17)

		for t in troops:
			troop = troops.index(t)
			if (troops[troop][1] - 1) % 18 + 1 <= tr:
				direc = findir([trind[troop][1], trind[troop][2]])
				pokemon[troops[troop][0] - 1].move(direc, trind[troop][0], trind[troop][1], trind[troop][2])
				pygame.draw.rect(gameDisplay, white, [trind[troop][1] - display_width//100, trind[troop][2] - display_height//100, display_width//25, display_height//140])
				pygame.draw.rect(gameDisplay, green, [trind[troop][1] - display_width//100, trind[troop][2] - display_height//100, (display_width//25 * trind[troop][3])//trind[troop][5], display_height//140])

				trind[troop][0] = (trind[troop][0] + 1) % 2

				if trind[troop][1] > -32 or 8*((troops[troop][1]-1)//18) == tim%timperwa:

					spe = trind[troop][4][2]

					if direc == 1:
						trind[troop][2] -= int((display_height//140) * (spe/240))
					elif direc == 2:
						trind[troop][1] += int((display_width//160) * (spe/240))
					elif direc == 3:
						trind[troop][2] += int((display_height//140) * (spe/240))
					else:
						trind[troop][1] -= int((display_width//160) * (spe/240))

				if trind[troop][1] > display_width:
					for projectile in projectiles:
						if projectile[3] == troop:
							projectiles.remove(projectile)
						elif projectile[3] > troop:
							projectile[3] -= 1

					trind.remove(trind[troop])
					troops.remove(troops[troop])
					crossed += 1

		for tem in range(len(towers)):
			tow = towers[tem]
			cen = [tow[0] + tower[tow[2]].l//2, tow[1] + tower[tow[2]].b//2]

			rang = tower[tow[2]].rang

			targ, maxx, maxy = -1, 0, 0

			if towtim[tem] == 0:
				for troop in range(len(troops)):
					troopco = [trind[troop][1], trind[troop][2]]

					if dist(cen, troopco) <= rang and maxx < trind[troop][1]:
						targ, maxx, maxy = troop, trind[troop][1], 0
					elif dist(cen, troopco) <= rang and maxx == troops[troop][1] and maxy < trind[troop][2]:
						targ, maxy = troop, trind[troop][2]

				if targ != -1:
					sound(projec[tower[tow[2]].projectile].relsound)
					projectiles.append([tower[tow[2]].projectile, tow[0] + tower[tow[2]].l//2, tow[1], targ, tem])
					towtim[tem]+=1

			else:
				towtim[tem] = (towtim[tem] + 1) % tower[tow[2]].tim

		for projectile in projectiles:
			x1, y1 = projectile[1], projectile[2]
			x2, y2 = trind[projectile[3]][1], trind[projectile[3]][2]
			if projectile[1] != trind[projectile[3]][1] or  projectile[2] != trind[projectile[3]][2]:

				ang = 0

				if x2 != x1:
					ang = atan(abs((y1 - y2)/(x2 - x1)))
				else:
					ang = pi/2

				if x2 > x1 and y2 < y1:
					ang = ang
				elif x2 < x1 and y2 < y1:
					ang = ang + pi/2
				elif x2 < x1 and y2 > y1:
					ang = ang + pi
				else:
					ang = ang + 3 * pi/2

				spe = projec[projectile[0]].speed
				img = projec[projectile[0]].rotim(ang*57.29577)

				if dist([x1, y1], [x2, y2]) > spe:
					projectile[1], projectile[2] = projectile[1] + spe*cos(ang), projectile[2] - spe*sin(ang)

				else:
					projectile[1], projectile[2] = x2, y2

				image(img, projectile[1], projectile[2]+projec[projectile[0]].b)
			
			tem = projectile[4]

			if dist([x1, y1], [towers[tem][0]+tower[towers[tem][2]].l//2, towers[tem][1]+tower[towers[tem][2]].b//2]) > tower[towers[tem][2]].rang:
				projectiles.remove(projectile)
			elif projectile[1] == x2 and projectile[2] == y2:
				sound(projec[projectile[0]].hitsound)
				for tr in trind:
					troop = trind.index(tr)
					if dist([tr[1], tr[2]], [projectile[1], projectile[2]]) <= projec[projectile[0]].areadamage:
						tr[3] -= ((tower[towers[projectile[4]][2]].attack * projec[projectile[0]].damage)//tr[4][1])

						if tr[3] <= 0:
							trind.remove(trind[troop])
							troops.remove(troops[troop])

							for project in projectiles:
								if project[3] == troop and project != projectile:
									projectiles.remove(project)
								elif project[3] > troop:
									project[3] -= 1


				projectiles.remove(projectile)


		if crossed >= 20 or len(troops)==0:
			projectiles.clear()
			troops.clear()

			colpatch(black, display_width, display_height, 168, 0, 0)

			pygame.draw.rect(gameDisplay, brown, [display_width//4, display_height//3, display_width//2, display_height//3])
			if crossed >= 20:
				writes("Escapers Won", sky_blue, display_width//4 + display_width//12, display_height//3 + display_height//20, display_height//25)
			else:
				writes("Defenders Won", sky_blue, display_width//4 + display_width//6, display_height//3 + display_height//20, display_height//25)

			

		tim += 1
		tr = tim // timperwa

		clock.tick(fram)

		pygame.display.update()