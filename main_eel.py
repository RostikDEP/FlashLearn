import eel, time
from utils import Database

dbController = Database("words.db")
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





eel.start("tabs.html")
# time.sleep(2)
