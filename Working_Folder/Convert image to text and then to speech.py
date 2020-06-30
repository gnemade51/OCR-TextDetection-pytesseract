#pip install the following - pytesseract and engine too check for proper path, pyttsx3, googletrans, pywin32
# import the following libraries
# will convert the image to text string
import pytesseract
# adds image processing capabilities
from PIL import Image
# converts the text to speech
import pyttsx3
# translates into the mentioned language
from googletrans import Translator

# opening an image from the source path
img = Image.open('bigsleep.jpg')
# describes image format in the output
print(img)
# path where the tesseract module is installed
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR/tesseract.exe'
# converts the image to result and saves it into result variable
result = pytesseract.image_to_string(img)
# write text in a text file and save it to source path
with open('abc.txt', mode='w') as file:
    file.write(result)
    print(result)

p = Translator()
# translates the text into hindi language
k = p.translate(result, dest='hindi')
print(k)
engine = pyttsx3.init()

# an audio will be played which speaks the test if pyttsx3 recognizes it
engine.say(result)
engine.runAndWait()
