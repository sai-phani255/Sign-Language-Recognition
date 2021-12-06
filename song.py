import glob
import os

i=2
while i>1:

    os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

    import pygame
    songs = glob.glob("voice/Y.mp3")
    import random

    song = random.choice(songs)

    pygame.mixer.init()

    music = pygame.mixer.music.load(song)
    pygame.mixer.music.play()

    print(i)

    time = 0
    while (pygame.mixer_music.get_busy()):
        pygame.time.Clock().tick(10)
        time+=1
        #keyboard.add_hotkey("ctrl + s", lambda: pygame.mixer_music.stop())
        if time == 14:
            pygame.mixer_music.stop()
            time = 0
        #break
