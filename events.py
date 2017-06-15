import pygame
class Stats(object):


	def __init__(self):
		self.sleep = 3
		self.hunger = 3
		self.mood = 3
		self.hydration = 3
		self.cash = 120

	def pee_event(self):
		event_pic = "random_events/negative_1.png"
		self.hydration = 0
		self.mood -= 2
		self.cash -= 50
		if self.cash < 0:
			self.cash = 0
		if self.mood > 1:
			self.mood -= 1
		else:
			self.mood = 0

		if self.mood < 0:
			self.mood = 0

		effect = pygame.mixer.Sound('sounds/happiness_down.wav')
		effect.play()

		return event_pic

	def keyboard_break_event(self):
		event_pic = "random_events/negative_2.png"
		self.cash = self.cash - 30
		self.mood -= 2
		if self.cash < 0:
			self.cash = 0

		effect = pygame.mixer.Sound('sounds/happiness_down.wav')
		effect.play()

		return event_pic

	def police_event(self):
		event_pic = "random_events/negative_3.png"
		self.cash = self.cash - 150
		self.mood -= 2
		if self.cash < 0:
			self.cash = 0

		if self.mood > 1:
			self.mood -= 1
		else:
			self.mood = 0

		if self.sleep > 1:
			self.sleep -= 1
		else:
			self.sleep = 0

		effect = pygame.mixer.Sound('sounds/happiness_down.wav')
		effect.play()

		return event_pic

	def bitcoin_event(self):
		event_pic = "random_events/positive_1.png"
		self.cash += 150
		self.mood = 3

		effect = pygame.mixer.Sound('sounds/happiness_up.wav')
		effect.play()

		return event_pic

	def keyboard_eat_event(self):
		event_pic = "random_events/positive_2.png"

		self.hunger = 3

		self.mood = 3

		effect = pygame.mixer.Sound('sounds/happiness_up.wav')
		effect.play()

		return event_pic

	def meme_event(self):
		event_pic = "random_events/positive_3.png"
		self.mood = 3
		self.cash += 50

		effect = pygame.mixer.Sound('sounds/happiness_up.wav')
		effect.play()

		return event_pic
