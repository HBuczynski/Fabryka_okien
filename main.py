# -*- coding: utf-8 -*-

import Database
from datetime import date, timedelta

# Polaczenie z baza danych
db = Database.Database()
# Ponowne utworzenie bazy
db.recreate()

db.add_model("Bozenka")
db.add_segment("Bozenka", "Segment 1", 1, 2, 3)
db.add_segment("Bozenka", "Segment 2", 4, 5, 6)
db.add_param("Bozenka", "Segment 1", "Kolor", "Kolor segmentu")
db.add_param_value("Bozenka", "Segment 1", "Kolor", "Czerwony")
db.add_windowpane("3-komorowa", 3.14)
db.add_windowpane("2-komorowa", 2.14)
db.add_windowpane("1-komorowa", 1.14)
db.add_client_person("Janusz", "Mel", "Powstancow MELu 1/6", "94121221212")
db.add_client_company("MEL", "Melowa 12/3", "12345678900")
db.add_bill(1, 123000, date.today(), date.today()+timedelta(days=10), "Zlozone")
db.add_bill_entry(1, 1, 1, 100, 200, 3, 0, 'Zlozone')
db.add_delivery(1, "Testowa 1/2", 120.50, 15)
db.add_installation(1, 400.00, date.today()+timedelta(days=20))

db.commit()

# Zakonczenie polaczenia z baza
db.close()