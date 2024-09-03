import eel, time
from utils import Database, ConfigProcessor

dbController = Database("words.db")
confProc = ConfigProcessor()

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
def AreaRecognize():
    print("Hello")


eel.start("tabs.html")
# time.sleep(2)
