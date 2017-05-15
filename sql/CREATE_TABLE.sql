use Fabryka_okien;

DROP TABLE IF EXISTS Dostawa;
DROP TABLE IF EXISTS Montaz;
DROP TABLE IF EXISTS Staty_miesiac;
DROP TABLE IF EXISTS Staty_klienta;
DROP TABLE IF EXISTS Parametr_pozycji;
DROP TABLE IF EXISTS Wartosc_parametru;
DROP TABLE IF EXISTS Parametr_segmentu;
DROP TABLE IF EXISTS Pozycja;
DROP TABLE IF EXISTS Faktura;
DROP TABLE IF EXISTS Klient;
DROP TABLE IF EXISTS Segment;
DROP TABLE IF EXISTS Szyba;
DROP TABLE IF EXISTS Model;


CREATE TABLE Model (
model_id INTEGER PRIMARY KEY AUTO_INCREMENT,
nazwa VARCHAR(20) NOT NULL UNIQUE
);

CREATE TABLE Segment (
segment_id INTEGER NOT NULL AUTO_INCREMENT,
nazwa VARCHAR(20) NOT NULL UNIQUE,
cena_b NUMERIC(5,1) DEFAULT 1,
cena_c NUMERIC(5,1) DEFAULT 1,
cena_d NUMERIC(5,1) DEFAULT 1,
czas_produkcji INTEGER DEFAULT 7,
model_id INTEGER NOT NULL,
czy_aktualny ENUM('Aktualny','Wycofany') DEFAULT 'Aktualny',
CONSTRAINT PK_Segment PRIMARY KEY (segment_id), 
FOREIGN KEY (model_id) REFERENCES Model (model_id) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE Parametr_segmentu (
parametr_id INTEGER PRIMARY KEY AUTO_INCREMENT,
nazwa VARCHAR(20) NOT NULL,
segment_id INTEGER NOT NULL,
opis VARCHAR(100),
CONSTRAINT FK_Parametr FOREIGN KEY (segment_id) REFERENCES Segment (segment_id)
ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Wartosc_parametru (
id INTEGER PRIMARY KEY AUTO_INCREMENT,
wartosc VARCHAR(20) NOT NULL,
parametr_id INTEGER NOT NULL,
opis VARCHAR(100),
CONSTRAINT FK_Wartosc FOREIGN KEY (parametr_id) REFERENCES Parametr_segmentu (parametr_id)
ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Szyba (
szyba_id INTEGER PRIMARY KEY AUTO_INCREMENT,
rodzaj VARCHAR(20) NOT NULL,
cena_a NUMERIC(5,1) DEFAULT 1
);

CREATE TABLE Klient (
klient_id INTEGER PRIMARY KEY AUTO_INCREMENT,
selektor ENUM('Osoba prywatna', 'Firma'),
adres_faktury VARCHAR(50) NOT NULL,
imie VARCHAR(20),
nazwisko VARCHAR(20),
pesel VARCHAR(11) UNIQUE,
nip VARCHAR(11) UNIQUE,
nazwa VARCHAR(30)
);

CREATE TABLE Faktura (
faktura_id INTEGER PRIMARY KEY AUTO_INCREMENT,
data_dodania DATE NOT NULL,
cena_suma NUMERIC(16,2) NOT NULL DEFAULT 0,
klient_id INTEGER,
adres_faktury VARCHAR(50) NOT NULL,
imie VARCHAR(20),
nazwisko VARCHAR(20),
pesel VARCHAR(11),
nip VARCHAR(11),
nazwa VARCHAR(30),
czas_zakonczenia DATE,
status ENUM('Zlozone', 'Anulowane', 'W trakcie realizacji', 'Gotowe', 'Zakonczone', 'Zwrot') DEFAULT 'Zlozone',
FOREIGN KEY (klient_id) REFERENCES Klient (klient_id)
ON DELETE SET NULL ON UPDATE CASCADE
);

CREATE TABLE Dostawa (
adres_dostawy VARCHAR(50) NOT NULL,
cena_dostawy NUMERIC(7,2),
faktura_id INTEGER PRIMARY KEY,
czas_dostawy INTEGER DEFAULT 7,
FOREIGN KEY (faktura_id) REFERENCES Faktura (faktura_id)
ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Montaz (
faktura_id INTEGER PRIMARY KEY,
data_montazu DATE NOT NULL,
cena_montazu NUMERIC(7,2),
FOREIGN KEY (faktura_id) REFERENCES Faktura (faktura_id)
ON DELETE CASCADE ON UPDATE CASCADE	
);

CREATE OR REPLACE VIEW firmav1 AS
    SELECT
        Klient.klient_id,
        Klient.adres_faktury,
        Klient.nip,
        Klient.nazwa
    FROM
        Klient
    WHERE
	selektor='Firma';

CREATE OR REPLACE VIEW osobav1 AS
    SELECT
        Klient.klient_id,
        Klient.adres_faktury,
        Klient.imie,
        Klient.nazwisko,
        Klient.pesel
    FROM
        Klient
    WHERE
	selektor='Osoba prywatna';

CREATE TABLE Staty_klienta (
klient_id INTEGER NOT NULL,
rok INTEGER NOT NULL,
miesiac INTEGER NOT NULL,
suma NUMERIC(16,2) NOT NULL,
CONSTRAINT PK_Staty_klienta PRIMARY KEY (klient_id, rok, miesiac),
CONSTRAINT FK_Staty_klienta FOREIGN KEY (klient_id) REFERENCES Klient (klient_id)
ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Pozycja (
pozycja_id            INTEGER NOT NULL AUTO_INCREMENT,
wymiar_x              NUMERIC(6,0) NOT NULL,
wymiar_y              NUMERIC(6,0) NOT NULL,
ilosc                 INTEGER NOT NULL DEFAULT 1,
cena_jednostkowa      NUMERIC(16,2),
faktura_id            INTEGER NOT NULL,
segment_id            INTEGER NOT NULL,
szyba_id              INTEGER NOT NULL,
status                ENUM('Zlozone', 'W trakcie realizacji', 'Wyslane/odebrane', 'Gotowe') DEFAULT 'Zlozone',
CONSTRAINT PK_Pozycja PRIMARY KEY (pozycja_id, faktura_id),
CONSTRAINT FK_Pozycja_faktura FOREIGN KEY (faktura_id) REFERENCES Faktura (faktura_id)
ON DELETE CASCADE ON UPDATE CASCADE,
CONSTRAINT FK_Pozycja_segment FOREIGN KEY (segment_id) REFERENCES Segment (segment_id)
ON DELETE RESTRICT ON UPDATE CASCADE,
CONSTRAINT FK_Pozycja_szyba FOREIGN KEY (szyba_id) REFERENCES Szyba (szyba_id)
ON DELETE RESTRICT ON UPDATE RESTRICT
);

CREATE TABLE Parametr_pozycji (
pozycja_id INTEGER NOT NULL,
faktura_id INTEGER NOT NULL,
wartosc_id INTEGER NOT NULL,
CONSTRAINT FK_Parametr_pozycji_poz FOREIGN KEY (pozycja_id, faktura_id) REFERENCES Pozycja(pozycja_id, faktura_id)
ON DELETE CASCADE ON UPDATE CASCADE,
CONSTRAINT FK_Parametr_pozycji_wart FOREIGN KEY (wartosc_id) REFERENCES Wartosc_parametru (id)
ON DELETE RESTRICT ON UPDATE CASCADE
);

CREATE TABLE Staty_miesiac (
rok INTEGER NOT NULL,
miesiac INTEGER NOT NULL,
suma NUMERIC (16,2) NOT NULL,
CONSTRAINT PK_Staty_miesiac PRIMARY KEY (rok, miesiac)
);

