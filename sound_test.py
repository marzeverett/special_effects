import time
import pygame
import random

pygame.mixer.init()
pygame.mixer.music.load('sounds/thunder.mp3')

sleep_time = 1.5


group_1_actions = ["clock", "erratic_flowers", "shaking_box", "knock_over"]
group_2_actions = ["thunder", "glass"]
finish_action = ["lantern"]



def play_sound(what_sound):
        sound_string = 'sounds/'+what_sound+".mp3"
        pygame.mixer.init()
        pygame.mixer.music.load(sound_string)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            pass
        #print(dev_id)



print(random.randrange(2, 5))
#play_sound("wand_finish")