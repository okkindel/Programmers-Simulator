import pygame
import random
from pygame.locals import *
from events import Stats


class RandomEvent(object):

	def __init__(self):
		self.stats = Stats()

	def bad_event(self):
		event_pic = "random_events/empty_box.png"
		if self.stats.hydration < 2:
			event_pic = self.stats.pee_event()
		elif self.stats.mood > 2:
			event_pic = self.stats.kayboard_break_event()
		elif self.stats.sleep > 2:
			event_pic = self.stats.police_event()
		return event_pic

	def good_event(self):
		event_pic = "random_events/empty_box.png"
		if self.stats.sleep > 2:
			event_pic = self.stats.bitcoin_event()
		elif self.stats.hunger < 1:
			event_pic = self.stats.keyboard_eat_event()
		elif self.stats.mood > 1:
			event_pic = self.stats.meme_event()
		return event_pic

	def event_type(self):
		event_pic = "random_events/empty_box.png"

		if random.choice([True, False]):
			event_pic = self.bad_event()
		else:
			event_pic = self.good_event()
		return event_pic

	def event_chance(self):
		event_pic = "random_events/empty_box.png"
		if random.choice([True, False]):
			event_pic = self.event_type()
		return event_pic





