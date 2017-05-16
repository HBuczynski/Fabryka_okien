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

# Zakonczenie polaczenia z baza
db.close()