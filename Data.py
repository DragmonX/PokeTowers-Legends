from propervalues import *
import pygame, time, random

pygame.init()

#hard coding

tilesize = display_height//11

# importing images

tile = loadimage('Images/tile.jpeg', tilesize, tilesize)

#Datas

class Tower():
	def __init__(self, file_name, l, b, rang, projectile, tim, attack, cost):
		self.img = loadimage(file_name, l, b)
		self.l = l
		self.b = b
		self.rang = rang
		self.projectile = projectile
		self.tim = tim
		self.attack = attack
		self.cost = cost

	def dis(self, x, y):
		boxed(self.img, x, y, self.l, self.b)

tower = [  Tower("Images/placement.png", display_width//20, display_width//20, 0, 0, 0, 0, 0)
		 , Tower("Images/archertower.png", display_height//11, display_height//11, 3 * tilesize, "Arrow", 13, 100, 2000)
		 , Tower("Images/cannontower.png", display_height//11, display_height//11, int(2.5 * tilesize), "Bomb", 26, 80, 1800)
		 , Tower("Images/teslatower.png", display_height//11, display_height//11, 4 * tilesize, "Bolt", 4, 64, 1500)
		 ]

class SpriteSheet(object):
    def __init__(self, file_name, x, y, row, col):
	    self.sprite_sheet = pygame.image.load(file_name)
	    self.height = x
	    self.width = y
	    self.row = row
	    self.col = col

    def get_image(self, num):
	    image = pygame.Surface([self.width, self.height])

	    y = int(num / self.col) * self.height
	    x = num % self.col * self.width

	    image.blit(self.sprite_sheet, (0, 0), (x, y, self.width, self.height))
	    image.set_colorkey(black)

	    return image

sprite = [	SpriteSheet("Images/pokemon.png", 32, 32, 40, 18)
		  , SpriteSheet("Images/archer.png", 32, 32, 4, 13)
		]

class Pokemon():
	def __init__(self, name, moveleft, movedown, moveup, moveright, hp, speed, attack, defence):
		self.moveset = [moveup, moveright, movedown, moveleft]
		self.name = name
		self.hp = hp
		self.speed = speed
		self.attack = attack
		self.defence = defence
		self.cost = 2*(hp+attack//4+defence+speed//2)

	def move(self, direc, ind, x, y):
		image(sprite[0].get_image(self.moveset[direc - 1][ind] - 1), x, y)
	
	def healthp(self, iv):
		health = int(2 * self.hp + 2  * iv + 100 + 5)
		return health
		
	def stats(self, iv):
		rand = int((random.randrange(85, 100) / 1.0) * 1.0)
		rand = rand / 100
	
		mattack = int((2 * self.attack + 2 * iv) * rand + 5)
		mdefence = int(2 * self.defence + 2 * iv + 5)
		mspeed = int(2 * self.speed +  2 * iv + 5)
		
		stat = [mattack, mdefence, mspeed]
		return stat


pokemon = [	 Pokemon("Chespin", [2, 20], [37, 55], [1, 19], [38, 56], 56, 38, 61, 65)
		   , Pokemon("Quilladin", [4, 22], [39, 57], [3, 21], [40, 58], 61, 57, 78, 95)
		   , Pokemon("Chesnaught", [6, 24], [41, 59], [5, 23], [42, 60], 98, 64, 107, 122)
		   , Pokemon("Fennekin", [8, 26], [43, 61], [7, 25], [44, 62], 40, 60, 62, 60)
		   , Pokemon("Braixen", [10, 28], [45, 63], [9, 27], [46, 64], 59, 73, 90, 70)
		   , Pokemon("Delphox", [12, 30], [47, 65], [11, 29], [48, 66], 76, 104, 114, 100)
		   , Pokemon("Froakie", [14, 32], [49, 67], [13, 31], [50, 68], 41, 71, 62, 44)
		   , Pokemon("Frogadier", [16, 34], [51, 69], [15, 33], [52, 70], 54, 97, 83, 56)
		   , Pokemon("Greninja", [18, 36], [53, 71], [17, 35], [54, 72], 72, 132, 153, 71)
		   , Pokemon("Bunnelby", [74, 92], [109, 127], [73, 91], [110, 128], 38, 57, 36, 38)
		   , Pokemon("Diggersby", [76, 94], [111, 129], [75, 93], [112, 130], 85, 78, 56, 77)
		   , Pokemon("Fletchling", [78, 96], [113, 131], [77, 95], [114, 132], 45, 52, 50, 43)
		   , Pokemon("Fletchinder", [80, 98], [115, 133], [79, 97], [116, 134], 62, 84, 73, 55)
		   , Pokemon("Talonflame", [82, 100], [117, 135], [81, 99], [118, 136], 78, 126, 81, 71)
		]

class Projectile():
	def __init__(self, img, l, b, initor, speed, aread, damage, hitsound, relsound):
		self.img = loadimage(img, l, b)
		self.l = l
		self.b = b
		self.initor = initor
		self.speed = speed
		self.areadamage = aread
		self.damage = damage
		self.hitsound = loadsound(hitsound)
		self.relsound = loadsound(relsound)

	def rotim(self, ang):
		im = self.img
		return pygame.transform.rotate(im, ang-self.initor)

projec = {   "Arrow":Projectile("Images/arrow.png", 30, 6, 0, 40, 0, 130, "Sound/hitarrow.wav", "Sound/releasearrow.wav")
		   , "Bomb":Projectile("Images/bomb.png", 15, 15, 0, 20, 60, 180, "Sound/explosion.wav", None)
		   , "Bolt":Projectile("Images/bolt.png", 30, 54, 90, 50, 0, 50, None, "Sound/lightning.wav")
		 }