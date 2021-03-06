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
        if selector == "Imię i nazwisko" and search_line != '':
            search_line_imie = ''.join(map(str,search_line.split(" ")[0]))
            search_line_nazwisko = ''.join(map(str,search_line.split(" ")[1]))
            query = ("SELECT klient_id, adres_faktury, imie, nazwisko, nip, pesel, nazwa FROM Klient"
                     " WHERE imie=%s  AND nazwisko=%s")
            self.cursor.execute(query, (search_line_imie, search_line_nazwisko))
        elif search_line == '':
            query = ("SELECT klient_id, adres_faktury, imie, nazwisko, nip, pesel, nazwa FROM Klient ")
            self.cursor.execute(query)
        else:
            query = ("SELECT klient_id, adres_faktury, imie, nazwisko, nip, pesel, nazwa FROM Klient "
                     "WHERE %s='%s'" % (selector, search_line))
            self.cursor.execute(query)
        return self.cursor.fetchall()

    def get_invoices(self, selector, search_line, data_from, data_to, status):
        if search_line != '' and status != 'wszystko':
            query = ("SELECT faktura_id, klient_id, adres_faktury, data_dodania, czas_zakonczenia, status, cena_suma FROM Faktura "
                     "WHERE %s = '%s' AND data_dodania > '%s' AND czas_zakonczenia < '%s' AND status = '%s'" %
                     (selector, search_line, data_from, data_to, status))
            self.cursor.execute(query)
        elif search_line == '' and status == "wszystko":
            query = ("SELECT faktura_id, klient_id, adres_faktury, data_dodania, czas_zakonczenia, status, cena_suma "
                     "FROM Faktura")
            print(query)
            self.cursor.execute(query)
        elif status == "wszystko" and search_line != '':
            query = ("SELECT faktura_id, klient_id, adres_faktury, data_dodania, czas_zakonczenia, status, cena_suma FROM Faktura "
            "WHERE %s = '%s' AND data_dodania > '%s' AND czas_zakonczenia < '%s'" % (selector, search_line, data_from, data_to))
            self.cursor.execute(query)
        elif status != "wszystko" and search_line == '':
            query=("SELECT faktura_id, klient_id, adres_faktury, data_dodania, czas_zakonczenia, status, cena_suma FROM Faktura " \
            "WHERE data_dodania > '%s' AND czas_zakonczenia < '%s' AND status = '%s'" % (data_from, data_to, status))
            self.cursor.execute(query)
        return self.cursor.fetchall()

    def get_month_report(self,data_from_month, data_from_year, data_to_month, data_to_year):
        query = ("SELECT rok, miesiac, suma FROM Staty_miesiac "
                 "WHERE rok >= '%s' AND rok <= '%s' OR rok = '%s' AND rok = '%s' AND miesiac >= '%s' AND miesiac <= '%s'"
                 % (data_from_year, data_to_year, data_from_year, data_to_year, data_from_month, data_to_month))
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def get_client_report(self,selector, search_line, data_from_year, data_from_month, data_to_year, data_to_month):
        if selector == "Imię i nazwisko" and search_line != '':
            search_line_imie = ''.join(map(str,search_line.split(" ")[0]))
            search_line_nazwisko = ''.join(map(str,search_line.split(" ")[1]))
            query = ("SELECT klient_id, rok, miesiac, suma FROM Staty_klienta"
                     " WHERE imie=%s  AND nazwisko=%s "
                     "AND rok >= %s AND rok <= %s OR rok = %s AND rok = %s AND miesiac >= %s AND miesiac <= %s" %
                     (search_line_imie, search_line_nazwisko, data_from_year, data_to_year,
                      data_from_year, data_to_year, data_from_month, data_to_month))
            print(query)
            self.cursor.execute(query)
        elif search_line == '':
            query = ("SELECT klient_id, rok, miesiac, suma FROM Staty_klienta "
                     "WHERE rok >= %s AND rok <= %s OR rok = %s AND rok = %s AND miesiac >= %s AND miesiac <= %s" %
                     (data_from_year, data_to_year,data_from_year,data_to_year, data_from_month, data_to_month))
            print(query)
            self.cursor.execute(query)
        else:
            query = ("SELECT klient_id, rok, miesiac, suma FROM Staty_klienta "
                     "WHERE %s=%s "
                     "AND rok >= %s AND rok <= %s OR rok = %s AND rok = %s AND miesiac >= %s AND miesiac <= %s"
                     % (selector, search_line, data_from_year, data_to_year, data_from_year, data_to_year,data_from_month, data_to_month))
            print(query)
            self.cursor.execute(query)
        return self.cursor.fetchall()

    def update_client_person(self, name, surname, pesel, address, id):
        query = ("UPDATE Klient SET imie = '%s', nazwisko = '%s', pesel = '%s', adres_faktury = '%s' WHERE klient_id = '%s'" %
                 (name, surname, pesel, address,id[0]))
        self.cursor.execute(query)

    def update_client_company(self, cmp_name, cmp_nip, cmp_address, id):
        query = ("UPDATE Klient SET nazwa = '%s', nip = '%s', adres_faktury = '%s' WHERE klient_id = '%s'" %
                 (cmp_name, cmp_nip, cmp_address, id[0]))
        self.cursor.execute(query)

    def get_model_id(self, nazwa_modelu):
        query = ("SELECT model_id FROM Model "
                 "WHERE nazwa=%s")
        self.cursor.execute(query, (nazwa_modelu,))
        return self.cursor.fetchone()[0]

    def get_models(self):
        query = ("SELECT nazwa, model_id FROM Model")
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def get_segments(self, model_id):
        query = ("SELECT nazwa, segment_id FROM Segment "
                 "WHERE model_id=%s")
        self.cursor.execute(query, (model_id,))
        return self.cursor.fetchall()

    def get_params(self, segment_id):
        query = ("SELECT nazwa, parametr_id, opis FROM Parametr_segmentu "
                 "WHERE segment_id=%s")
        self.cursor.execute(query, (segment_id,))
        return self.cursor.fetchall()

    def get_vals(self, parametr_id):
        query = ("SELECT wartosc, id FROM Wartosc_parametru "
                 "WHERE parametr_id=%s")
        self.cursor.execute(query, (parametr_id,))
        return self.cursor.fetchall()

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

    def del_model(self, model_id):
        query = ("UPDATE Segment SET czy_aktualny = 'Wycofany'"
                 "WHERE model_id=%s")
        self.cursor.execute(query, (model_id,))

    def del_segment(self, segment_id):
        query = ("UPDATE Segment SET czy_aktualny = 'Wycofany'"
                 "WHERE segment_id=%s")
        self.cursor.execute(query, (segment_id,))

    def is_segment_active(self, segment_id):
        query = ("SELECT czy_aktualny FROM Segment "
                 "WHERE segment_id=%s")
        self.cursor.execute(query, (segment_id,))
        return self.cursor.fetchone()[0] == 'Aktualny'

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

    def del_param(self, parametr_id):
        query = ("DELETE FROM Parametr_segmentu "
                 "WHERE parametr_id=%s")
        self.cursor.execute(query, (parametr_id,))

    def del_value(self, value_id):
        query = ("DELETE FROM Wartosc_parametru "
                 "WHERE id=%s")
        self.cursor.execute(query, (value_id,))

    def add_windowpane(self, rodzaj_szyby, cena_a):
        query = ("INSERT INTO Szyba "
                 "(rodzaj, cena_a) "
                 "VALUES (%s,%s)")
        self.cursor.execute(query, (rodzaj_szyby, cena_a))

    def add_client_person(self, imie, nazwisko, pesel, adres_faktury):
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

    def get_positions_from_invoice(self, faktura_id):
        query = ("SELECT pozycja_id, segment_id, cena_jednostkowa, wymiar_x, wymiar_y, ilosc, status FROM Pozycja WHERE faktura_id={FAKTURA}".format(FAKTURA=faktura_id))
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def get_model_name(self, model_id):
        query = ("SELECT nazwa FROM Model WHERE model_id={ID}".format(ID=model_id))
        self.cursor.execute(query)
        return self.cursor.fetchone()[0]

    def get_segment_name_and_modelid(self, segment_id):
        query = ("SELECT nazwa, model_id FROM Segment WHERE segment_id={SEGMENT}".format(SEGMENT=segment_id))
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def is_client_company(self, faktura_id):
        query = ("SELECT k.selektor FROM Klient AS k "
                 "INNER JOIN Faktura AS f ON k.klient_id = f.klient_id "
                 "WHERE f.faktura_id = %s")
        self.cursor.execute(query, ((faktura_id,)))
        return self.cursor.fetchone()[0] == "Firma"

    def check_delivery(self, faktura_id):
        query = ("SELECT cena_dostawy FROM Dostawa "
                 "WHERE faktura_id=%s")
        self.cursor.execute(query, (faktura_id,))
        return self.cursor.fetchone()

    def check_assembly(self, faktura_id):
        query = ("SELECT cena_montazu FROM Montaz "
                 "WHERE faktura_id=%s")
        self.cursor.execute(query, (faktura_id,))
        return self.cursor.fetchone()

    def get_rodzaj_szyby(self):
        query = "SELECT rodzaj FROM Szyba"
        self.cursor.execute(query)
        return self.cursor.fetchall()

# Global database instance
db = Database()
