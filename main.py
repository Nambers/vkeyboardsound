import threading

import keyboard
import pygame.mixer

tmp = []


def playSound(s: pygame.mixer.Sound):
    s.play()


def hook(event: keyboard.KeyboardEvent):
    if event.event_type == "down":
        if event.name in tmp:
            return
        press()
        tmp.append(event.name)
    else:
        release()
        tmp.remove(event.name)


def press():
    global press_sound
    threading.Thread(target=playSound, args=[press_sound]).start()


def release():
    global release_sound
    threading.Thread(target=playSound, args=[release_sound]).start()


if __name__ == '__main__':
    pygame.mixer.pre_init()
    pygame.mixer.init()
    press_sound = pygame.mixer.Sound("press.mp3")
    release_sound = pygame.mixer.Sound("release.mp3")
    keyboard.hook(hook)
    keyboard.wait()
