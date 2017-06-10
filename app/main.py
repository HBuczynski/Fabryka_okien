import sys

#from datetime import date, timedelta
#from generator import Database
from app.gui import *

if __name__ == "__main__":
    #Connecting to database:

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())