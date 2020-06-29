from pydub import AudioSegment
from pydub.playback import play
from picamera import PiCamera
from PIL import Image
from gtts import gTTS
from time import sleep
import pytesseract
import wave

camera = PiCamera()

camera.start_preview()
sleep(5)
camera.capture('basic.jpg')
camera.stop_preview()

im = Image.open("basic.jpg")

text = pytesseract.image_to_string(im, lang = 'eng')

print(text)

tts = gTTS(text)
tts.save('basic.wav')

sound = AudioSegment.from_mp3('basic.wav')
play(sound)
