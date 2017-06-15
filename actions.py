import pygame
from pygame.locals import *
import time

def sleep(events, gameDisplay):

	events.stats.sleep = 3
	events.stats.mood += 1
	if events.stats.mood > 3:
		events.stats.mood = 3
	events.stats.hunger -= 1
	if events.stats.hunger < 0:
		events.stats.hunger = 0
	effect = pygame.mixer.Sound('sounds/energy.wav')
	effect.play()
	
	time.sleep(0.5)

def pee(events, gameDisplay):

	events.stats.hunger -= 1
	events.stats.hydration = 3
	events.stats.mood += 1
	if events.stats.mood > 3:
		events.stats.mood = 3
	if events.stats.hydration > 3:
		events.stats.hydration = 3
	if events.stats.hunger < 0:
		events.stats.hunger = 0
	effect = pygame.mixer.Sound('sounds/hunger.wav')
	effect.play()
	
	time.sleep(0.5)

def computer(events, gameDisplay):

	events.stats.mood -= 1
	events.stats.cash += 50
	if events.stats.mood < 0:
		events.stats.mood = 0
	if events.stats.cash < 0:
		events.stats.cash = 0
	events.stats.hunger -= 1
	events.stats.hydration -= 1
	if events.stats.hunger < 0:
		events.stats.hunger = 0
	if events.stats.hydration < 0:
		events.stats.hydration = 0
	events.stats.sleep -= 1
	if events.stats.sleep < 0:
		events.stats.sleep = 0


def fridge(events, gameDisplay):
	pos = (0, 0);
	fridge_meal = 0
	fridge_costs = 0

	fridge_menu = pygame.image.load('pop_up_window/fridge.png')
	gameDisplay.blit(fridge_menu, (60, 50))

	pygame.display.update()

	done = False

	while not done and events.stats.cash > 20:
		ev = pygame.event.get()

		for event in ev:
			if event.type == pygame.MOUSEBUTTONUP:
				pos = pygame.mouse.get_pos()
      			if pos[0] > 70 and pos[0] < 210 and pos[1] > 94 and pos[1] < 130 and events.stats.cash >= 20:
      				fridge_meal = 1
      				fridge_costs = 10
      				done = True
      			elif pos[0] > 70 and pos[0] < 210 and pos[1] > 150 and pos[1] < 195 and events.stats.cash >= 20:
      				fridge_meal = 2
      				fridge_costs = 20
      				done = True
      			elif pos[0] > 210 and pos[0] < 346 and pos[1] > 94 and pos[1] < 130 and events.stats.cash >= 30:
      				fridge_meal = 2
      				fridge_costs = 30
      				done = True
      			elif pos[0] > 210 and pos[0] < 346 and pos[1] > 150 and pos[1] < 185 and events.stats.cash >= 40:
      				fridge_meal = 3
      				fridge_costs = 40
      				done = True

	events.stats.mood += 1
	if events.stats.mood > 3:
		events.stats.mood = 3
	events.stats.cash -= fridge_costs
	if events.stats.cash < 0:
		events.stats.cash = 0
	events.stats.hunger += fridge_meal
	if events.stats.hunger > 3:
		events.stats.hunger = 3
	events.stats.hydration -= 1
	if events.stats.hydration < 0:
		events.stats.hydration = 0
	effect = pygame.mixer.Sound('sounds/action.wav')
	effect.play()

	time.sleep(0.5)	