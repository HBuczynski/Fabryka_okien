from datetime import date, timedelta
import random
import Database

NAMES = ["Beata", "Anna", "Magda", "Zosia", "Karolina", "Grazyna", "Alicja", "Kasia", "Monika"]

# Liczba generowanych danych
N_MODELS = 3
N_MAXSEGMENTS = 5

class Generator:
    def __init__(self, database: Database.Database):
        self.db = database

    def generate(self):
        print("Generating random data...")

        # Wybierz N_MODELS unikalnych nazw z bazy nazw modeli
        model_names = [NAMES[i] for i in random.sample(range(len(NAMES)), N_MODELS)]

        for model_name in model_names:
            print("ADD_MODEL: " + model_name)
            self.db.add_model(model_name)
            model_id = self.db.get_model_id(model_name)

            segment_names = self.generateSegments()
            for segment_name in segment_names:
                print("\tADD_SEGMENT: " + segment_name)
                self.db.add_segment(model_name, segment_name, self.generateCenaB(), self.generateCenaC(),
                                    self.generateCenaD())
                segment_id = self.db.get_segment_id(model_name, segment_name)

    def generateSegments(self):
        return ["Segment " + chr(i + 64) for i in range(1, random.randint(2, N_MAXSEGMENTS))]

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



