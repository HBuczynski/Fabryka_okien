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
        return 0

    def generateCenaB(self):
        return 0

    def generateCenaC(self):
        return 0

    def generateCenaD(self):
        return 0



