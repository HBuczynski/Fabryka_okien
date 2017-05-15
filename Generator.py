from datetime import date, timedelta
import random
import Database

NAMES = ["Beata", "Anna", "Magda", "Zosia", "Karolina", "Grazyna", "Alicja", "Kasia", "Monika"]
PARAMS = [["Kolor segmentu", ["Czerwony", "Zielony", "Źólty", "Brązowy", "Biały", "Szary", "Niebieski"]],
          ["Typ drewna", ["Buk", "Sosna", "Dąb", "Jesion", "Świerk", "Modrzew"]],
          #...
          ]

# Liczba generowanych danych
N_MODELS = 3
N_MAXSEGMENTS = 5
N_MAXPARAMS = 2

class Generator:
    def __init__(self, database: Database.Database):
        self.db = database

    def generate(self):
        # Generowanie oferty (modele, segmenty, parametry, wartosci)
        self.generate_stock()
        # Generowanie klientow
        self.generate_clients()
        # Generowanie zamowien
        self.generate_orders()

    def generate_stock(self):
        print("Generating random data...")

        # Wybierz N_MODELS unikalnych nazw z bazy nazw modeli
        model_names = self.generate_names()

        for model_name in model_names:
            print("ADD_MODEL: " + model_name)
            self.db.add_model(model_name)
            model_id = self.db.get_model_id(model_name)

            segment_names = self.generate_segments()
            for segment_name in segment_names:
                print("\tADD_SEGMENT: " + segment_name)
                self.db.add_segment(model_name, segment_name, self.generateCenaB(), self.generateCenaC(),
                                    self.generateCenaD())
                segment_id = self.db.get_segment_id(model_name, segment_name)

                parameters = self.generate_parameters()
                for parameter in parameters:
                    print("\t\tADD PARAM: " + parameter[0])

    def generate_clients(self):
        pass
        # TODO

    def generate_orders(self):
        pass
        # TODO

    def generate_names(self):
        return [NAMES[i] for i in random.sample(range(len(NAMES)), N_MODELS)]

    def generate_segments(self):
        return ["Segment " + chr(i + 64) for i in range(1, random.randint(2, N_MAXSEGMENTS))]

    def generate_parameters(self):
        return [PARAMS[i] for i in random.sample(range(len(PARAMS)), random.randint(0, N_MAXPARAMS))]

    def generateCenaA(self):
	random.seed()
	A = random.uniform(0.1,2.0)
	return float("{0:.1f}".format(A))

    def generateCenaB(self):
        random.seed()
	A = random.uniform(1.0,4.0)
	return float("{0:.1f}".format(A))

    def generateCenaC(self):
        random.seed()
	A = random.uniform(0.1,5.0)
	return float("{0:.1f}".format(A))

    def generateCenaD(self):
        random.seed()
	A = random.uniform(20.0,500.0)
	return float("{0:.1f}".format(A))



