import keyboard
import pygame

pygame.init()
pygame.mixer.init()

sound = pygame.mixer.Sound('keypress.wav')

# Flag to avoid sound repetition when a key is held down
sound_played = False

# Function to execute when a key is pressed
def play_sound(e):
    global sound_played
    if not sound_played and keyboard.is_pressed(e.name):
        sound.play()
        sound_played = True
    elif sound_played and not keyboard.is_pressed(e.name):
        sound_played = False

# Attach the function to any key press event
keyboard.hook(play_sound)

# Keep the script running
keyboard.wait('esc')