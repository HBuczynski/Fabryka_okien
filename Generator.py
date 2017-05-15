from datetime import date, timedelta
import random
import Database

PARAMS = [["Kolor segmentu", "Kolor farby, jaka pokryte sa malowane elementy segmentu.", ["Czerwony", "Zielony", "Zolty", "Brazowy", "Bialy", "Szary", "Niebieski"]],
          ["Typ drewna", "Material, z ktorego wykonane sa drewniane elementy segmentu.", ["Buk", "Sosna", "Dab", "Jesion", "Swierk", "Modrzew"]],
          ["Okucie", "Typ okucia wykorzystywany w segmencie.", ["Standardowe", "Antywlamaniowe"]],
          ["Uchylne", "Wybor czy okno moze sie uchylac, czy nie.", ["Tak", "Nie"]],
          ["Otwierane","Wybor czy okno moze sie otwierac i w ktora strone.", ["Prawe", "Lewe", "Nieotwieralne"]],
          ["Kolor uszczelki","Wybot koloru uszczelki segmentu", ["Czarna", "Braz", "Biala", "Zlota"]],
          ["Szprosy", "Wybor rozkladu szprosow", ["1 na 1", "2 na 2", "3 na 2", "3 na 3", "Brak"]]
          ]
ADDRESSES = ["Krucza", "Lesna", "Dluga", "Szeroka", "Polna", "Jana Sobieskiego", "Kwiatowa", "Koszykowa", "Noakowskiego", "Aleja Komisji Edukacji Narodowej", "Grojecka", "Pulawska"]

# Liczba generowanych danych
N_MODELS = 3
N_MAXSEGMENTS = 5
N_MAXPARAMS = 2

class Generator:
    def __init__(self, database: Database.Database):
        self.db = database

        self.NAMES = self.load_names()


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
            print("ADD MODEL: " + model_name)
            self.db.add_model(model_name)
            model_id = self.db.get_model_id(model_name)

            segment_names = self.generate_segments()
            for segment_name in segment_names:
                print(" ADD SEGMENT: " + segment_name)
                self.db.add_segment_by_id(model_id, segment_name, self.generateCenaB(), self.generateCenaC(),
                                    self.generateCenaD())
                segment_id = self.db.get_segment_id(model_name, segment_name)

                parameters = self.generate_parameters()
                for parameter in parameters:
                    print("  ADD PARAM: " + parameter[0])
                    self.db.add_param_by_id(segment_id, parameter[0], parameter[1])
                    parameter_id = self.db.get_parametr_id(model_name, segment_name, parameter[0])

                    values = parameter[2]
                    for value in values:
                        print("   ADD VALUE: " + value)
                        self.db.add_param_value_by_id(parameter_id, value)

    def generate_clients(self):
        pass
        # TODO

    def generate_orders(self):
        pass
        # TODO

    def generate_names(self):
        return [self.NAMES[i] for i in random.sample(range(len(self.NAMES)), N_MODELS)]

    def generate_segments(self):
        return ["Segment " + chr(i + 64) for i in range(1, random.randint(2, N_MAXSEGMENTS))]

    def generate_parameters(self):
        return [PARAMS[i] for i in random.sample(range(len(PARAMS)), random.randint(0, N_MAXPARAMS))]

    def generate_person_name(self):
        return "Anna Kowalska"

    def generate_company_name(self):
        return "Pepsi"

    def generate_address(self):
        return random.choice(ADDRESSES) + " " + str(random.randint(1, 200))

    def generateCenaA(self):
        random.seed()
        A = random.uniform(0.1, 2.0)
        return float("{0:.1f}".format(A))

    def generateCenaB(self):
        random.seed()
        A = random.uniform(1.0, 4.0)
        return float("{0:.1f}".format(A))

    def generateCenaC(self):
        random.seed()
        A = random.uniform(0.1, 5.0)
        return float("{0:.1f}".format(A))

    def generateCenaD(self):
        random.seed()
        A = random.uniform(20.0, 500.0)
        return float("{0:.1f}".format(A))

    def load_names(self):
        names = []
        with open("./sql/imiona.txt") as file:
            for line in file:
                line = line.strip()
                names.append(line)
        return names

    def load_surnames(self):
        names = []
        with open("./sql/nazwiska.txt") as file:
            for line in file:
                line = line.strip()
                names.append(line)
        return names


