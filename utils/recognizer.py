import pyautogui
import pytesseract
import googletrans
class Recognizer:
    def __init__(self):
        pass


    def RecognizeText(self, x1, y1, x2, y2):
        screen = pyautogui.screenshot(region=(x1, y1, abs(x2-x1), abs(y2-y1)))
        text = pytesseract.image_to_string(screen).replace("\n"," ")
        return text


    def TranslateText(self, text):
        translator = googletrans.Translator()
        translation = translator.translate(text, dest='uk', src='en').text
        return translation