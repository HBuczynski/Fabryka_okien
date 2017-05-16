from datetime import date, timedelta
import random
import Database

# Liczba generowanych danych
N_MODELS = 3
N_MAXSEGMENTS = 5
N_MAXPARAMS = 2
N_PERSONS = 50
N_COMPANIES = 50

class Generator:
    def __init__(self, database: Database.Database):
        self.db = database

        # Zaladowanie danych slownikowych
        self.NAMES = self.load_names()
        self.SURNAMES = self.load_surnames()
        self.ADDRESSES = self.load_addresses()
        self.COMPANIES = self.load_companies()
        self.PARAMS = [["Kolor segmentu", "Kolor farby, jaka pokryte sa malowane elementy segmentu.", ["Czerwony", "Zielony", "Zolty", "Brazowy", "Bialy", "Szary", "Niebieski"]],
                      ["Typ drewna", "Material, z ktorego wykonane sa drewniane elementy segmentu.", ["Buk", "Sosna", "Dab", "Jesion", "Swierk", "Modrzew"]],
                      ["Okucie", "Typ okucia wykorzystywany w segmencie.", ["Standardowe", "Antywlamaniowe"]],
                      ["Uchylne", "Wybor czy okno moze sie uchylac, czy nie.", ["Tak", "Nie"]],
                      ["Otwierane","Wybor czy okno moze sie otwierac i w ktora strone.", ["Prawe", "Lewe", "Nieotwieralne"]],
                      ["Kolor uszczelki","Wybot koloru uszczelki segmentu", ["Czarna", "Braz", "Biala", "Zlota"]],
                      ["Szprosy", "Wybor rozkladu szprosow", ["1 na 1", "2 na 2", "3 na 2", "3 na 3", "Brak"]]]


    def generate(self):
        # Generowanie oferty (modele, segmenty, parametry, wartosci)
        print("===================== GENERATING STOCK   =====================")
        self.generate_stock()
        # Generowanie klientow
        print("===================== GENERATING CLIENTS =====================")
        self.generate_clients()
        # Generowanie zamowien
        print("===================== GENERATING ORDERS  =====================")
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
        names = self.generate_person_names()
        surnames = self.generate_person_surnames()
        addresses = [self.generate_address() for it in range(N_PERSONS)]
        pesels = self.generate_pesels()
        for i in range(N_PERSONS):
            print("ADD PERSON: ('%s', '%s', '%s', '%s')" % (names[i], surnames[i], addresses[i], pesels[i]))
            self.db.add_client_person(names[i], surnames[i], addresses[i], pesels[i])

        names = self.generate_company_names()
        addresses = [self.generate_address() for it in range(N_COMPANIES)]
        nips = self.generate_nips()
        for i in range(N_COMPANIES):
            print("ADD COMPANY: ('%s', '%s', '%s')" % (names[i], addresses[i], nips[i]))
            self.db.add_client_company(names[i], addresses[i], nips[i])


    def generate_orders(self):
        pass
        # TODO

    def generate_names(self):
        return [self.NAMES[i] for i in random.sample(range(len(self.NAMES)), N_MODELS)]

    def generate_segments(self):
        return ["Segment " + chr(i + 64) for i in range(1, random.randint(2, N_MAXSEGMENTS))]

    def generate_parameters(self):
        return [self.PARAMS[i] for i in random.sample(range(len(self.PARAMS)), random.randint(0, N_MAXPARAMS))]

    def generate_person_names(self):
        return [self.NAMES[i] for i in random.sample(range(len(self.NAMES)), N_PERSONS)]

    def generate_person_surnames(self):
        return [self.SURNAMES[i] for i in random.sample(range(len(self.SURNAMES)), N_PERSONS)]

    def generate_company_names(self):
        return [self.COMPANIES[i] for i in random.sample(range(len(self.COMPANIES)), N_COMPANIES)]

    def generate_pesels(self):
        return [str(50000000000 + i) for i in random.sample(range(50000000000), N_PERSONS)]

    def generate_nips(self):
        return [str(1000000000 + i) for i in random.sample(range(9000000000), N_COMPANIES)]

    def generate_address(self):
        return random.choice(self.ADDRESSES) + " " + str(random.randint(1, 200))

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

    def load_file(self, file):
        contents = []
        with open(file) as file:
            for line in file:
                line = line.strip()
                contents.append(line)
        return contents

    def load_names(self):
        return self.load_file("./sql/imiona.txt")

    def load_surnames(self):
        return self.load_file("./sql/nazwiska.txt")

    def load_addresses(self):
        return self.load_file("./sql/ulice.txt")

    def load_companies(self):
        return self.load_file("./sql/firmy.txt")

