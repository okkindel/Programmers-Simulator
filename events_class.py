import pygame
from pygame.locals import *

informationSquare = pygame.Rect(283, 378, 283, 378)
GREY_COLOR = (128,128,128)
popupFont = pygame.font.SysFont("Arial", 15, bold = False, italic = False)


class Stats(object):

	def __init__(self):
		self.sleep = 0
		self.hunger = 0
		self.mood = 0
		self.hydration = 0
		self.cash = 0

	def peeEvent(self):
		#komunikat że zapomniałeś o toalecie i nie wytrzymałeś presji nawodnienia :/ Obniża nawodnienie do 0 oraz płacisz 50$ za sprzątanie
		pygame.draw.rect(gameDisplay, GREY_COLOR, informationSquare)
		informationText = "Niestety praca pochlonela Cie za bardzo :/ Zapomniales o toalecie przez co pogorszył Ci sie nastroj(- 20) oraz koszty sprzatania wyniosly 50$ ale za to na plus masz oprozniony pecherz :)"
		gameDisplay.blit(popupFont.render(informationText, False, (0,0,0)), (300, 400))

		events.stats.hydration
		self.cash -= 50
		if self.mood > 20:
			self.mood -= 20
		else:
			self.mood = 0

	def keyboardBreakEvent(self):
		#komunikat że z nerwów podczas pracy rozwaliłeś klawiaturę, tracisz 30$
		pygame.draw.rect(gameDisplay, GREY_COLOR, informationSquare)
		informationText = "Humor nie ten? Zdarza sie. Szkoda ze klawiatura tego nie zrozumie, zas zakup nowej wyniesie Cie 30$"
		gameDisplay.blit(popupFont.render(informationText, False, (0,0,0)), (300, 400))
		self.cash = self.cash - 30

	def policeEvent(self):
		#komunikat że policja znalazła pirackie pliki na twoim komputerze, nastrój -30, hajs - 150, sen - 20
		pygame.draw.rect(gameDisplay, GREY_COLOR, informationSquare)
		informationText = "Pamietasz ostatni sezon Gry o Tron? Bo policja pamieta torrent z ktorego go pobrales. Niestety 150$ w plecy oraz stracony czas jak i humor :/"
		gameDisplay.blit(popupFont.render(informationText, False, (0,0,0)), (300, 400))
		self.cash = self.cash - 150

		if self.mood > 30:
			self.mood -= 30
		else:
			self.mood = 0

		if self.sleep > 20:
			self.sleep -= 20
		else:
			self.sleep = 0

	def bitcoinEvent(self):
		#komunikat że przypomniałeś sobie o swoim starym portfelu bitcoin więc poprawia Ci sie nastrój +20 i zarabiasz 100$
		pygame.draw.rect(gameDisplay, GREY_COLOR, informationSquare)
		informationText = "Elo"
		gameDisplay.blit(popupFont.render(informationText, False, (0,0,0)), (300, 400))
		self.cash += 100

		if self.mood < 81:
			self.mood += 20
		else:
			self.mood = 100

	def keyboardEatEvent(self):
		#komunikat o tym że znajdujesz kawałek pizzy w klawiaturze, jedzenie + 20 oraz nastrój + 15
		pygame.draw.rect(gameDisplay, GREY_COLOR, informationSquare)
		informationText = "Elo"
		gameDisplay.blit(popupFont.render(informationText, False, (0,0,0)), (300, 400))

		if self.hunger < 81:
			self.hunger += 20
		else:
			self.hunger = 100

		if self.mood < 86:
			self.mood += 15
		else:
			self.mood = 100

	def memeEvent(self):
		#komunikat że tworzysz smiesznego mema xD nastrój +30 wzrus jak i hajs + 5 wpadł na leczenie psychiatryczne
		pygame.draw.rect(gameDisplay, GREY_COLOR, informationSquare)
		informationText = "Elo"
		gameDisplay.blit(popupFont.render(informationText, False, (0,0,0)), (300, 400))

		if  self.mood < 71 :
			self.mood += 30
		else:
			self.mood = 100
		self.cash += 5
