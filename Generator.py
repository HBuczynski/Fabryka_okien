from datetime import date, timedelta
import random
import Database

# Liczba generowanych danych
N_MODELS = 40
N_MAXSEGMENTS = 20
N_MAXPARAMS = 2
N_PERSONS = 50
N_COMPANIES = 50
N_BILLS = 10
N_MAXBILLENTRIES = 20

PRINT_DEBUG = False

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
        print("Generating random data...")
        # Generowanie oferty (modele, segmenty, parametry, wartosci)
        print("===================== GENERATING STOCK   =====================")
        self.generate_stock()
        # Generowanie klientow`
        print("===================== GENERATING CLIENTS =====================")
        self.generate_clients()
        # Generowanie zamowien
        print("===================== GENERATING ORDERS  =====================")
        self.generate_orders()

        # Zapisanie danych do bazy
        self.db.commit()

    def generate_stock(self):
        # Wybierz N_MODELS unikalnych nazw z bazy nazw modeli
        model_names = self.generate_names()

        for model_name in model_names:
            if PRINT_DEBUG:
                print("ADD MODEL: " + model_name)
            self.db.add_model(model_name)
            model_id = self.db.get_model_id(model_name)

            segment_names = self.generate_segments()
            for segment_name in segment_names:
                if PRINT_DEBUG:
                    print(" ADD SEGMENT: " + segment_name)
                self.db.add_segment_by_id(model_id, segment_name, self.generateCenaB(), self.generateCenaC(),
                                    self.generateCenaD())
                segment_id = self.db.get_segment_id(model_name, segment_name)

                parameters = self.generate_parameters()
                for parameter in parameters:
                    if PRINT_DEBUG:
                        print("  ADD PARAM: " + parameter[0])
                    self.db.add_param_by_id(segment_id, parameter[0], parameter[1])
                    parameter_id = self.db.get_parametr_id(model_name, segment_name, parameter[0])

                    values = parameter[2]
                    for value in values:
                        if PRINT_DEBUG:
                            print("   ADD VALUE: " + value)
                        self.db.add_param_value_by_id(parameter_id, value)

        self.windowspanes_number = 3
        self.db.add_windowpane("1-komorowa", self.generateCenaA())
        self.db.add_windowpane("2-komorowa", self.generateCenaA())
        self.db.add_windowpane("3-komorowa", self.generateCenaA())

    def generate_clients(self):
        names = self.generate_person_names()
        surnames = self.generate_person_surnames()
        addresses = [self.generate_address() for it in range(N_PERSONS)]
        pesels = self.generate_pesels()
        for i in range(N_PERSONS):
            if PRINT_DEBUG:
                print("ADD PERSON: ('%s', '%s', '%s', '%s')" % (names[i], surnames[i], addresses[i], pesels[i]))
            self.db.add_client_person(names[i], surnames[i], addresses[i], pesels[i])

        names = self.generate_company_names()
        addresses = [self.generate_address() for it in range(N_COMPANIES)]
        nips = self.generate_nips()
        for i in range(N_COMPANIES):
            if PRINT_DEBUG:
                print("ADD COMPANY: ('%s', '%s', '%s')" % (names[i], addresses[i], nips[i]))
            self.db.add_client_company(names[i], addresses[i], nips[i])

    def generate_orders(self):
        for bill in range(N_BILLS):
            klient_id = self.generate_klient_id()
            date_added = date.today()+timedelta(days=random.randint(-10000, 10000))
            date_done = date_added+timedelta(days=random.randint(5, 30))
            if PRINT_DEBUG:
                print("ADD BILL: (klient_id: %d)" % (klient_id))

            bill_status = "Zlozone"
            self.db.add_bill(klient_id, date_added, date_done, bill_status)
            bill_id = self.db.get_bill_id(klient_id, date_added, date_done, bill_status)

            for entry in range(random.randint(1, N_MAXBILLENTRIES)):
                segment_id = self.generate_segment_id()
                if PRINT_DEBUG:
                    print(" ADD ENTRY: (segment_id: %d)" % (segment_id))
                dimX = self.generate_dimension()
                dimY = self.generate_dimension()
                count = random.randint(1, 10)
                status = "Zrealizowane"
                szyba_id = random.randint(1, self.windowspanes_number)
                self.db.add_bill_entry(bill_id, segment_id, szyba_id, dimX, dimY, count, status)
                entry_id = self.db.get_bill_entry_id(bill_id, segment_id, szyba_id, dimX, dimY, count, status)

                params = self.db.get_params_for_segment_id(segment_id)
                for param_id in params:
                    values = self.db.get_values_ids_for_param_id(param_id)
                    value_id = random.choice(values)
                    if PRINT_DEBUG:
                        print("  FOR PARAM: %s ADD VALUE: %s" % (param_id, value_id))
                    self.db.add_bill_entry_param_value(bill_id, value_id, entry_id)

            if random.randint(0, 1) == 0:
                self.db.add_delivery(bill_id, self.generate_address(), random.randint(100, 6000)/10,
                                     random.randint(5, 20))
            if random.randint(0, 2) == 0:
                self.db.add_installation(bill_id, random.randint(100, 6000)/10,
                                         date_done+timedelta(days=random.randint(5, 20)))


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

    def generate_klient_id(self):
        return self.db.get_random_klient_id()

    def generate_segment_id(self):
        return self.db.get_random_segment_id()

    def generate_dimension(self):
        return random.randrange(300, 3000, 10)

    def generateCenaA(self):
        random.seed()
        A = random.uniform(0.00001, 0.0001)
        return float("{0:.5f}".format(A))

    def generateCenaB(self):
        random.seed()
        A = random.uniform(0.01, 0.8)
        return float("{0:.5f}".format(A))

    def generateCenaC(self):
        random.seed()
        A = random.uniform(0.01, 0.5)
        return float("{0:.5f}".format(A))

    def generateCenaD(self):
        random.seed()
        A = random.uniform(2.0, 500.0)
        return float("{0:.5f}".format(A))

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

