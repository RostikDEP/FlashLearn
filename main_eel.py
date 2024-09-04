import eel, time
from utils import Database, ConfigProcessor, Recognizer

dbController = Database("words.db")
confProc = ConfigProcessor()
recognizer = Recognizer()

eel.init("html")

@eel.expose
def AddWord(word, translate, sentence):
    if word != "" and translate != "" and sentence != "":
        try:
            dbController.AddWord(word, translate, sentence)
        except:
            eel.FormBlink("red")
        else:
            eel.ClearInputs()
            eel.FormBlink("green")
    else:
        eel.FormBlink("red")


@eel.expose
def GetRandomWordPy():
    word = dbController.GetRandomWord()
    eel.setup_cardJS(word[1], word[2], word[3])


@eel.expose
def GetScreenConfig():
    cords = confProc.ReadData("configs/screen_coordinates.json")
    return cords

@eel.expose
def AreaRecognize(x1, y1, x2, y2):
    text = recognizer.RecognizeText(int(x1), int(y1), int(x2), int(y2))
    try:
        translation = recognizer.TranslateText(text)
    except:
        translation = "Не вдалося перекласти"
    eel.FillTextData(text, translation)


eel.start("tabs.html")
# time.sleep(2)
