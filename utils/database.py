import sqlite3


class Database:
    def __init__(self, path):
        self.db = sqlite3.connect(path)
        self.cursor = self.db.cursor()


    def AddWord(self, word, translate, sentence):
        self.cursor.execute("""INSERT INTO words (word, translate, sentence, entered, complete) VALUES (?, ?, ?, ?, ?) """, (word, translate, sentence, 0, 0))
        self.db.commit()