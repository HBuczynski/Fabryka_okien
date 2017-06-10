import sys
from generator import Database, Generator
from datetime import date, timedelta
from app.gui import *

if __name__ == "__main__":
    #Connecting to database:
    db = Database.Database()

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    db.close()
    sys.exit(app.exec_())


def clickedSearchClientButton(self):
    query = ("SELECT * FROM Faktury")
    self.cursor.execute(query)
    result = self.cursor.fetchall()
    print(result)