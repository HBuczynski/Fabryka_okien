import mysql.connector
from os import system
import random
import db_settings as DB

class Database:
    def __init__(self):
        self.cnx = mysql.connector.connect(user=DB.USER, password=DB.PASSWORD, host=DB.HOST, database=DB.DATABASE)
        self.cursor = self.cnx.cursor()

    @staticmethod
    def recreate():
        print("Recreating the database...")
        system("mysql -u " + DB.USER + " --password=" + DB.PASSWORD + " " + DB.DATABASE + " < ./sql/CREATE_TABLE.sql")
        system("mysql -u " + DB.USER + " --password=" + DB.PASSWORD + " " + DB.DATABASE + " < ./sql/CREATE_TRIGGER.sql")

    def commit(self):
        self.cnx.commit()

    def close(self):
        self.cnx.close()

    def get_clients(self,selector, search_line):
        if selector == "Imię i nazwisko":
            search_line_imie = ''.join(map(str,search_line.split(" ")[0]))
            search_line_nazwisko = ''.join(map(str,search_line.split(" ")[1]))
            query = ("SELECT klient_id, adres_faktury, imie, nazwisko, nip, pesel, nazwa FROM Klient"
                     " WHERE imie=%s  AND nazwisko=%s")
            self.cursor.execute(query, (search_line_imie, search_line_nazwisko))
        else:
            query = ("SELECT klient_id, adres_faktury, imie, nazwisko, nip, pesel, nazwa FROM Klient "
                     "WHERE %s='%s'" % (selector, search_line))
            self.cursor.execute(query)
        return self.cursor.fetchall()

    def get_model_id(self, nazwa_modelu):
        query = ("SELECT model_id FROM Model "
                 "WHERE nazwa=%s")
        self.cursor.execute(query, (nazwa_modelu,))
        return self.cursor.fetchone()[0]

    def get_segment_id(self, nazwa_modelu, nazwa_segmentu):
        query = ("SELECT segment_id FROM Segment "
                 "INNER JOIN Model ON Model.model_id=Segment.model_id "
                 "WHERE Model.nazwa=%s AND Segment.nazwa=%s")
        self.cursor.execute(query, (nazwa_modelu, nazwa_segmentu))
        return self.cursor.fetchone()[0]

    def get_parametr_id(self, nazwa_modelu, nazwa_segmentu, nazwa_parametru):
        query = ("SELECT parametr_id FROM Parametr_segmentu p "
                 "INNER JOIN Segment s ON p.segment_id=s.segment_id "
                 "WHERE p.nazwa=%s AND s.nazwa=%s AND s.model_id=(SELECT model_id FROM Model WHERE nazwa=%s)")
        self.cursor.execute(query, (nazwa_parametru, nazwa_segmentu, nazwa_modelu))
        return self.cursor.fetchone()[0]

    def get_bill_id(self, klient_id, data_dodania, czas_zakonczenia, status):
        query = ("SELECT faktura_id FROM Faktura "
                 "WHERE klient_id=%s AND data_dodania=%s AND czas_zakonczenia=%s AND status=%s")
        self.cursor.execute(query, (klient_id, data_dodania, czas_zakonczenia, status))
        return self.cursor.fetchone()[0]

    def get_bill_entry_id(self, faktura_id, segment_id, szyba_id, wymiar_x, wymiar_y, ilosc, status):
        query = ("SELECT pozycja_id FROM Pozycja "
                 "WHERE faktura_id=%s AND segment_id=%s AND szyba_id=%s AND wymiar_x=%s AND wymiar_y=%s AND ilosc=%s AND status=%s")
        self.cursor.execute(query, (faktura_id, segment_id, szyba_id, wymiar_x, wymiar_y, ilosc, status))
        return self.cursor.fetchone()[0]

    def get_params_for_segment_id(self, segment_id):
        query = ("SELECT parametr_id FROM Parametr_segmentu "
                 "WHERE segment_id=%s")
        self.cursor.execute(query, (segment_id,))
        result = self.cursor.fetchall()
        return [it[0] for it in result]

    def get_values_ids_for_param_id(self, parametr_id):
        query = ("SELECT id FROM Wartosc_parametru "
                 "WHERE parametr_id=%s")
        self.cursor.execute(query, (parametr_id,))
        result = self.cursor.fetchall()
        return [it[0] for it in result]

    def add_model(self, nazwa_modelu):
        query = ("INSERT INTO Model "
                 "(nazwa) "
                 "VALUES (%s)")
        self.cursor.execute(query, (nazwa_modelu,))

    def add_segment_by_id(self, model_id, nazwa_segmentu, cena_b, cena_c, cena_d):
        query = ("INSERT INTO Segment "
                 "(nazwa, cena_b, cena_c, cena_d, model_id) "
                 "VALUES (%s,%s,%s,%s,%s)")
        self.cursor.execute(query, (nazwa_segmentu, cena_b, cena_c, cena_d, model_id))

    def add_segment(self, nazwa_modelu, nazwa_segmentu, cena_b, cena_c, cena_d):
        self.add_segment_by_id(self.get_model_id(nazwa_modelu), nazwa_segmentu, cena_b, cena_c, cena_d)

    def add_param_by_id(self, segment_id, nazwa_parametru, opis_parametru):
        query = ("INSERT INTO Parametr_segmentu "
                 "(nazwa, segment_id, opis) "
                 "VALUES (%s,%s,%s)")
        self.cursor.execute(query, (nazwa_parametru, segment_id, opis_parametru))

    def add_param(self, nazwa_modelu, nazwa_segmentu, nazwa_parametru, opis_parametru):
        self.add_param_by_id(self.get_segment_id(nazwa_modelu, nazwa_segmentu), nazwa_parametru, opis_parametru)

    def add_param_value_by_id(self, parametr_id, wartosc_parametru):
        query = ("INSERT INTO Wartosc_parametru "
                 "(wartosc, parametr_id) "
                 "VALUES (%s,%s)")
        self.cursor.execute(query, (wartosc_parametru, parametr_id))

    def add_param_value(self, nazwa_modelu, nazwa_segmentu, nazwa_parametru, wartosc_parametru):
        self.add_param_value_by_id(self.get_parametr_id(nazwa_modelu, nazwa_segmentu, nazwa_parametru), wartosc_parametru)

    def add_windowpane(self, rodzaj_szyby, cena_a):
        query = ("INSERT INTO Szyba "
                 "(rodzaj, cena_a) "
                 "VALUES (%s,%s)")
        self.cursor.execute(query, (rodzaj_szyby, cena_a))

    def add_client_person(self, imie, nazwisko, adres_faktury, pesel):
        query = ("INSERT INTO Klient "
                 "(selektor, adres_faktury, imie, nazwisko, pesel) "
                 "VALUES ('Osoba prywatna',%s,%s,%s,%s)")
        self.cursor.execute(query, (adres_faktury, imie, nazwisko, pesel))

    def add_client_company(self, nazwa, adres_faktury, nip):
        query = ("INSERT INTO Klient "
                 "(selektor, adres_faktury, nazwa, nip) "
                 "VALUES ('Firma',%s,%s,%s)")
        self.cursor.execute(query, (adres_faktury, nazwa, nip))

    def add_bill(self, klient_id, data_dodania, czas_zakonczenia, status):
        query = ("INSERT INTO Faktura "
                 "(data_dodania, klient_id, czas_zakonczenia, status) "
                 "VALUES (%s,%s,%s,%s)")
        self.cursor.execute(query, (data_dodania, klient_id, czas_zakonczenia, status))

    def add_bill_entry(self, faktura_id, segment_id, szyba_id, wymiar_x, wymiar_y, ilosc, status):
        query = ("INSERT INTO Pozycja "
                 "(wymiar_x, wymiar_y, ilosc, faktura_id, segment_id, szyba_id, status) "
                 "VALUES (%s,%s,%s,%s,%s,%s,%s)")
        self.cursor.execute(query, (wymiar_x, wymiar_y, ilosc, faktura_id, segment_id, szyba_id, status))

    def add_delivery(self, faktura_id, adres_dostawy, cena_dostawy, czas_dostawy):
        query = ("INSERT INTO Dostawa "
                 "(adres_dostawy, cena_dostawy, faktura_id, czas_dostawy) "
                 "VALUES (%s,%s,%s,%s)")
        self.cursor.execute(query, (adres_dostawy, cena_dostawy, faktura_id, czas_dostawy))

    def add_installation(self, faktura_id, cena_montazu, data_montazu):
        query = ("INSERT INTO Montaz "
                 "(faktura_id, cena_montazu, data_montazu) "
                 "VALUES (%s,%s,%s)")
        self.cursor.execute(query, (faktura_id, cena_montazu, data_montazu))

    def add_bill_entry_param_value(self, faktura_id, wartosc_id, pozycja_id):
        query = ("INSERT INTO Parametr_pozycji "
                 "(faktura_id, wartosc_id, pozycja_id) "
                 "VALUES (%s,%s,%s)")
        self.cursor.execute(query, (faktura_id, wartosc_id, pozycja_id))

    def get_random_klient_id(self):
        query = ("SELECT klient_id FROM Klient")
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return random.choice(result)[0]

    def get_random_segment_id(self):
        query = ("SELECT segment_id FROM Segment")
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return random.choice(result)[0]