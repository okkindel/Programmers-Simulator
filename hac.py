
import pygame
import time
import itertools
from randomEvents import RandomEvent
import actions

pygame.init()

file = 'sounds/background.wav'
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play(-1)

display_width = 1920
display_height = 1050
BORDER_EAST = display_width - 615  
BORDER_WEST = 535   
BORDER_NORTH = 60   
BORDER_SOUTH = display_height - 200
STEP = 25

BATTERIES_STATS = ['pop_up_window/lvl_null.png', 'pop_up_window/lvl_low.png', 'pop_up_window/lvl_medium.png', 'pop_up_window/lvl_high.png']
DOLLARS_NUMBERS = ['cash/0.png', 'cash/1.png', 'cash/2.png', 'cash/3.png', 'cash/4.png', 'cash/5.png', 'cash/6.png', 'cash/7.png', 'cash/8.png', 'cash/9.png', 'cash/dolar.png',]

class Item(object):
    def __init__(self, b, e, src, name, interaction = None):
        self.b =  b
        self.e  = b[0]+e[0], b[1]+e[1]
        self.image = pygame.image.load(src)
        self.interaction = interaction
        self.name = name
        print b[0], e[0], b[1], e[1], b[0]+e[0], b[1]+e[1]

    def draw(self, surface):
        surface.blit(self.image, self.b)

    def on(self, x, y):
        return self.b[0] < x+50 < self.e[0] and self.b[1] < y+180 < self.e[1]
    def iteract(self, events, gameDisplay):
        #font = pygame.font.Font("freesansbold.ttf", 30)
        #label2 = font.render("Score target not met", 1, (0,255,0))
        self.interaction(events, gameDisplay)

class Character(Item):
    def __init__(self, b, e, src_l, src_r, src_sr, src_sl,):
        self.b =  b
        self.e = e
        self.images_l = itertools.cycle([pygame.image.load(image) for image in src_l])
        self.images_r = itertools.cycle([pygame.image.load(image) for image in src_r])
        self.images_sr = itertools.cycle([pygame.image.load(image) for image in src_sr])
        self.images_sl = itertools.cycle([pygame.image.load(image) for image in src_sl])
        self.image = next(self.images_l)
        

    def move(self, x, y):
        is_right = self.b[0] < x
        #is_up = b[1] < y
        

        if self.b[0] < x:
            self.image = next(self.images_r)
            is_right = True
        elif self.b[0] > x:
            self.image = next(self.images_l)
            is_right = False
        elif self.b[1] < y:
            self.image = next(self.images_r)
        elif self.b[1] > y:
            self.image = next(self.images_l)
        if self.b[0] == x and self.b[1] == y:       
            if is_right == True:
                self.image = next(self.images_sr)
            else:
                self.image = next(self.images_sl)

        self.b = x, y

def draw_stats(gameDisplay, events):
    stats_img = pygame.image.load('pop_up_window/stats.png')
    gameDisplay.blit(stats_img, (1560, 50))
    battery_img = pygame.image.load(BATTERIES_STATS[events.stats.hunger])
    gameDisplay.blit(battery_img, (1624, 95))
    battery_img = pygame.image.load(BATTERIES_STATS[events.stats.sleep])
    gameDisplay.blit(battery_img, (1727, 95))
    battery_img = pygame.image.load(BATTERIES_STATS[events.stats.hydration])
    gameDisplay.blit(battery_img, (1803, 95))
    battery_img = pygame.image.load(BATTERIES_STATS[events.stats.mood])
    gameDisplay.blit(battery_img, (1727, 135))
    

    dollars_amount = events.stats.cash
    
    if dollars_amount > 1000:
        dollars_amount = 500
    
    dollar_img = pygame.image.load(DOLLARS_NUMBERS[dollars_amount / 100])
    gameDisplay.blit(dollar_img, (1618, 140))

    dollars_amount %= 100
    dollar_img = pygame.image.load(DOLLARS_NUMBERS[dollars_amount / 10])
    gameDisplay.blit(dollar_img, (1632, 140))

    dollars_amount %= 10
    dollar_img = pygame.image.load(DOLLARS_NUMBERS[dollars_amount])
    gameDisplay.blit(dollar_img, (1646, 140))

    dollar_img = pygame.image.load(DOLLARS_NUMBERS[10])
    gameDisplay.blit(dollar_img, (1660, 140))




gameDisplay = pygame.display.set_mode((display_width,display_height))
randomevent = RandomEvent()
pygame.display.set_caption('PROgramer s live')

clock = pygame.time.Clock()
clock.tick(60)
crashed = False

black = (0,0,0)
white = (255,255,255)

imgR = [ 'character/character_r1.png', 'character/character_r2.png', 'character/character_r3.png', 'character/character_r4.png', 'character/character_r5.png' ]
imgL = [ 'character/character_l1.png', 'character/character_l2.png', 'character/character_l3.png', 'character/character_l4.png', 'character/character_l5.png' ]
imgSL = [ 'character/character_l0.png', 'character/character_l1.png' ]
imgSR = [ 'character/character_r0.png', 'character/character_r1.png' ]

charImg = Character((500, 500), None, imgL, imgR, imgSR, imgSL,)
floorImg = Item((0,0), (display_width,display_height), 'background/background.png', "floor")
item_list = [
    Item((700,200), (272,176), 'assets/computer_on.png',  "computer", actions.computer),
    Item((1270,750), (115,137), 'assets/toilet.png', "toilet", actions.pee),       
    Item((535, 600), (112,236), 'assets/fridge.png', "fridge", actions.fridge),
    Item((1242, 200), (143,240), 'assets/bed.png', "bed", actions.sleep),
    ]

x, y = tmp_x, tmp_y = 990, 525

events = RandomEvent()

i = 0
while not crashed:  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
    floorImg.draw(gameDisplay)
    
    
    for item in item_list:
        item.draw(gameDisplay) 
        
    charImg.draw(gameDisplay)
    draw_stats(gameDisplay, events)

    pressed = pygame.key.get_pressed()
    time.sleep(0.05)

    if pressed[pygame.K_RIGHT]:
    	tmp_x = x + STEP
        tmp_x = min(tmp_x, BORDER_EAST)
        if item_list[-1].name == "img":
                item_list.pop() 
    	
    if pressed[pygame.K_LEFT]:
    	tmp_x = x - STEP
        tmp_x = max(tmp_x, BORDER_WEST)
        for item in item_list:
            if(item.name == "img_end"):
                exit() 
    	
    if pressed[pygame.K_UP]:
    	tmp_y = y - STEP
        tmp_y = max(tmp_y, BORDER_NORTH)
    	
    if pressed[pygame.K_DOWN]:
    	tmp_y = y + STEP
        tmp_y = min(tmp_y, BORDER_SOUTH)
    
    

    for item in item_list:
        if item.on(tmp_x, tmp_y):
            item.iteract(events, gameDisplay)
            if item.name == 'bed':
                tmp_x = x - 100
            if item.name == 'toilet':
                tmp_x = x - 80
            if item.name == 'computer':
                tmp_y = y + 50
               
                    
                item_list.append( Item((60, 50), (5,5),events.event_chance(), "img", None)) 
                
            if item.name == 'fridge':
                tmp_x = x + 50
                break
    else:
        x, y = tmp_x, tmp_y
             
    charImg.move(x, y)
    
    if events.stats.hunger == 0 or events.stats.sleep == 0:
        
        item_list.append(Item((60,50),(300,100), 'pop_up_window/dead.png', "img_end", None))


    pygame.display.update()
    clock.tick(50)
