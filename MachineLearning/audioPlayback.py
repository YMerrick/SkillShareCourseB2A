from playsound import playsound
import pyglet


file = 'audio/when.mp3'
playsound(file)
sound = pyglet.media.load('audio/system-fault.mp3',streaming = False)
sound.play()
