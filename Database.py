import mysql.connector
from os import system
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

    def add_bill(self, klient_id, cena_suma, data_dodania, czas_zakonczenia, status):
        query = ("INSERT INTO Faktura "
                 "(data_dodania, cena_suma, klient_id, czas_zakonczenia, status) "
                 "VALUES (%s,%s,%s,%s,%s)")
        self.cursor.execute(query, (data_dodania, cena_suma, klient_id, czas_zakonczenia, status))

    def add_bill_entry(self, faktura_id, segment_id, szyba_id, wymiar_x, wymiar_y, ilosc, cena_jednostkowa, status):
        query = ("INSERT INTO Pozycja "
                 "(wymiar_x, wymiar_y, ilosc, cena_jednostkowa, faktura_id, segment_id, szyba_id, status) "
                 "VALUES (%s,%s,%s,%s,%s,%s,%s,%s)")
        self.cursor.execute(query, (wymiar_x, wymiar_y, ilosc, cena_jednostkowa, faktura_id, segment_id, szyba_id,
                                    status))

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