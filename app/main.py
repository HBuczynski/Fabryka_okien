import sys
#import Database

from datetime import date, timedelta
from generator import Database
from app.gui import *

if __name__ == "__main__":
    #Connecting to database:

    app = QApplication(sys.argv)
    window = MainWindow()
    window.db = Database.Database()
    window.show()

    window.db.close()
    sys.exit(app.exec_())