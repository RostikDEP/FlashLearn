from utils import Database

dbController = Database("words.db")
# dbController.AddWord("Word", "Переклад", "Речення")
dbController.GetRandomWord()