# -*- coding: utf-8 -*-

import Database, Generator
from datetime import date, timedelta

# Polaczenie z baza danych
db = Database.Database()
# Ponowne utworzenie bazy
db.recreate()

# Wygenerowanie danych testowych
gen = Generator.Generator(db)
gen.generate()


db.add_bill(1, date.today(), date.today()+timedelta(days=10), "Zlozone")
bill_id = db.get_bill_id(1, date.today(), date.today()+timedelta(days=10), "Zlozone")
db.add_bill_entry(bill_id, 1, 1, 100, 200, 1, "Zlozone")

query = ("UPDATE Pozycja SET status='Zrealizowane'")
db.cursor.execute(query)

db.commit()

# Zakonczenie polaczenia z baza
db.close()