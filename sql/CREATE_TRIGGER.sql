-- Po dodaniu nowej pozycji zliczenie ceny jednostkowej pozycji oraz zaktualizowanie ceny faktury.

DROP TRIGGER IF EXISTS Nowy_segm;

DELIMITER //

CREATE TRIGGER Nowy_segm BEFORE INSERT ON Pozycja
FOR EACH ROW
       BEGIN
	DECLARE A NUMERIC;
	DECLARE B NUMERIC;
	DECLARE C NUMERIC;
	DECLARE D NUMERIC;

       SET @A := (SELECT cena_a FROM Szyba WHERE szyba_id=NEW.szyba_id);
       SET @B := (SELECT cena_b from Segment WHERE segment_id=NEW.segment_id);
       SET @C := (SELECT cena_c from Segment WHERE segment_id=NEW.segment_id);
       SET @D := (SELECT cena_d from Segment WHERE segment_id=NEW.segment_id);
	 SET NEW.cena_jednostkowa := @A*NEW.wymiar_x*NEW.wymiar_y+@B*NEW.wymiar_x+@D;

	UPDATE Faktura SET cena_suma = cena_suma + NEW.cena_jednostkowa*NEW.ilosc WHERE faktura_id=NEW.faktura_id;
       END;
//
DELIMITER ;

-- Update ceny jednostkowej oraz sumarycznej faktury po zmianach w segmencie.

DROP TRIGGER IF EXISTS Update_segm;

DELIMITER //

CREATE TRIGGER Update_segm BEFORE UPDATE ON Pozycja
FOR EACH ROW
       BEGIN
	DECLARE A NUMERIC;
	DECLARE B NUMERIC;
	DECLARE C NUMERIC;
	DECLARE D NUMERIC;

       SET @A := (SELECT cena_a FROM Szyba WHERE szyba_id=NEW.szyba_id);
       SET @B := (SELECT cena_b from Segment WHERE segment_id=NEW.segment_id);
       SET @C := (SELECT cena_c from Segment WHERE segment_id=NEW.segment_id);
       SET @D := (SELECT cena_d from Segment WHERE segment_id=NEW.segment_id);
	 SET NEW.cena_jednostkowa := @A*NEW.wymiar_x*NEW.wymiar_y+@B*NEW.wymiar_x+@D;

	UPDATE Faktura SET cena_suma = cena_suma - OLD.cena_jednostkowa*OLD.ilosc + NEW.cena_jednostkowa*NEW.ilosc WHERE faktura_id=OLD.faktura_id;
	 
       END;
//
DELIMITER ;

-- Zmiana ceny faktury po usunięciu pozycji z faktury.

DROP TRIGGER IF EXISTS Usuniety_segm;
DELIMITER //
CREATE TRIGGER Usuniety_segm AFTER DELETE ON Pozycja
FOR EACH ROW
       BEGIN
	DECLARE A NUMERIC;
	
	SET @A := OLD.cena_jednostkowa*OLD.ilosc;
 	
	UPDATE Faktura SET cena_suma = cena_suma - @A WHERE faktura_id=OLD.faktura_id;
       END;
//
DELIMITER ;

DROP TRIGGER IF EXISTS Auto_klient;
DELIMITER //
CREATE TRIGGER Auto_klient BEFORE INSERT ON Faktura
FOR EACH ROW
BEGIN   
	SET NEW.adres_faktury := (SELECT adres_faktury from Klient where klient_id=NEW.klient_id);
	SET NEW.imie :=(SELECT Klient.imie from Klient where klient_id=NEW.klient_id);
	SET NEW.nazwisko := (SELECT nazwisko from Klient where klient_id=NEW.klient_id);
	SET NEW.pesel:=(SELECT pesel from Klient where klient_id=NEW.klient_id);
	SET NEW.nip:=(SELECT nip from Klient where klient_id=NEW.klient_id);
	SET NEW.nazwa:=(SELECT nazwa from Klient where klient_id=NEW.klient_id);
 END;
//
DELIMITER ;

-- Dodanie ceny montażu do ceny faktury.

DROP TRIGGER IF EXISTS Cena_sum_mont;
DELIMITER //
CREATE TRIGGER Cena_sum_mont AFTER INSERT ON Montaz
FOR EACH ROW
       BEGIN
	UPDATE Faktura SET cena_suma = cena_suma + NEW.cena_montazu WHERE faktura_id=NEW.faktura_id;
       END;
//
DELIMITER ;

-- Dodanie ceny dostawy do ceny faktury.

DROP TRIGGER IF EXISTS Cena_sum_dost;
DELIMITER //
CREATE TRIGGER Cena_sum_dost AFTER INSERT ON Dostawa
FOR EACH ROW
       BEGIN
	UPDATE Faktura SET cena_suma = cena_suma + NEW.cena_dostawy WHERE faktura_id=NEW.faktura_id;
       END;
//
DELIMITER ;

DROP TRIGGER IF EXISTS Cena_sum_dost_update;
DELIMITER //
CREATE TRIGGER Cena_sum_dost_update AFTER UPDATE ON Dostawa
FOR EACH ROW
       BEGIN
	UPDATE Faktura SET cena_suma = cena_suma + NEW.cena_dostawy - OLD.cena_dostawy WHERE faktura_id=NEW.faktura_id;
       END;
//
DELIMITER ;

DROP TRIGGER IF EXISTS Cena_sum_dost_delete;
DELIMITER //
CREATE TRIGGER Cena_sum_dost_delete AFTER DELETE ON Dostawa
FOR EACH ROW
       BEGIN
	UPDATE Faktura SET cena_suma = cena_suma - OLD.cena_dostawy WHERE faktura_id=OLD.faktura_id;
       END;
//
DELIMITER ;

DROP TRIGGER IF EXISTS Staty_klienta;

DELIMITER //
CREATE TRIGGER Staty_klienta 
AFTER UPDATE ON Faktura FOR EACH ROW
BEGIN
IF NEW.status = 'Zakonczone' AND OLD.status<>NEW.status THEN
-- Statystyka ogólna:
UPDATE Staty_klienta SET suma := suma + NEW.cena_suma WHERE rok=0 AND klient_id=NEW.klient_id;
IF (SELECT COUNT(*) FROM Staty_klienta WHERE klient_id=NEW.klient_id)=0 THEN
INSERT INTO Staty_klienta (klient_id,rok,miesiac,suma) VALUES (NEW.klient_id,0,0,NEW.cena_suma);
END IF;
-- Statystyka roczna:
UPDATE Staty_klienta SET suma := suma + NEW.cena_suma WHERE miesiac=0 AND rok=YEAR(NEW.czas_zakonczenia) AND klient_id=NEW.klient_id;
IF(SELECT COUNT(*) FROM Staty_klienta WHERE rok=YEAR(NEW.czas_zakonczenia))=0 THEN
INSERT INTO Staty_klienta (klient_id,rok,miesiac,suma) VALUES (NEW.klient_id,YEAR(NEW.czas_zakonczenia),0,NEW.cena_suma);
END IF;
-- Statystyka miesieczna:
UPDATE Staty_klienta SET suma := suma + NEW.cena_suma WHERE miesiac=MONTH(NEW.czas_zakonczenia) AND rok=YEAR(NEW.czas_zakonczenia) AND klient_id=NEW.klient_id;
IF (SELECT COUNT(*) FROM Staty_klienta WHERE rok=YEAR(NEW.czas_zakonczenia) AND miesiac=MONTH(NEW.czas_zakonczenia))=0 THEN
INSERT INTO Staty_klienta (klient_id,rok,miesiac,suma) VALUES (NEW.klient_id,YEAR(NEW.czas_zakonczenia),MONTH(NEW.czas_zakonczenia),NEW.cena_suma);
END IF;
END IF;
END;
//
DELIMITER ; 

DROP TRIGGER IF EXISTS Staty_miesiac;

DELIMITER //
CREATE TRIGGER Staty_miesiac
AFTER UPDATE ON Faktura FOR EACH ROW
BEGIN
IF NEW.status = 'Zakonczone' AND OLD.status<>NEW.status THEN
-- Statystyka ogólna:
UPDATE Staty_miesiac SET suma := suma + NEW.cena_suma WHERE rok=0;
IF (SELECT COUNT(*) FROM Staty_miesiac)=0 THEN
INSERT INTO Staty_miesiac (rok,miesiac,suma) VALUES (0,0,NEW.cena_suma);
END IF;
-- Statystyka roczna:
UPDATE Staty_miesiac SET suma := suma + NEW.cena_suma WHERE miesiac=0 AND rok=YEAR(NEW.czas_zakonczenia);
IF(SELECT COUNT(*) FROM Staty_miesiac WHERE rok=YEAR(NEW.czas_zakonczenia))=0 THEN
INSERT INTO Staty_miesiac (rok,miesiac,suma) VALUES (YEAR(NEW.czas_zakonczenia),0,NEW.cena_suma);
END IF;
-- Statystyka miesieczna:
UPDATE Staty_miesiac SET suma := suma + NEW.cena_suma WHERE miesiac=MONTH(NEW.czas_zakonczenia) AND rok=YEAR(NEW.czas_zakonczenia);
IF (SELECT COUNT(*) FROM Staty_miesiac WHERE rok=YEAR(NEW.czas_zakonczenia) AND miesiac=MONTH(NEW.czas_zakonczenia))=0 THEN
INSERT INTO Staty_miesiac (rok,miesiac,suma) VALUES (YEAR(NEW.czas_zakonczenia),MONTH(NEW.czas_zakonczenia),NEW.cena_suma);
END IF;
END IF;
END;
//
DELIMITER ; 

DROP TRIGGER IF EXISTS Param_poz;

DELIMITER //

CREATE TRIGGER Param_poz
BEFORE INSERT ON Parametr_pozycji FOR EACH ROW
BEGIN
DECLARE ID_segm INTEGER;
DECLARE ID_wart INTEGER;
DECLARE ID_param INTEGER;

SET @ID_wart := (SELECT id from Wartosc_parametru WHERE id = NEW.wartosc_id);
SET @ID_param := (SELECT parametr_id from Wartosc_parametru WHERE id=@ID_wart); 
SET @ID_segm := (SELECT segment_id from Parametr_segmentu WHERE parametr_id = @ID_param);

IF @ID_segm <> (SELECT segment_id from Pozycja WHERE pozycja_id=NEW.pozycja_id AND faktura_id=NEW.faktura_id) THEN
SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Nieprawidlowy parametr dla danego segmentu';
END IF;
END;
//
DELIMITER ;

DROP TRIGGER IF EXISTS Param_poz_update;

DELIMITER //

CREATE TRIGGER Param_poz_update
BEFORE UPDATE ON Parametr_pozycji FOR EACH ROW
BEGIN
DECLARE ID_segm INTEGER;
DECLARE ID_wart INTEGER;
DECLARE ID_param INTEGER;

SET @ID_wart := (SELECT id from Wartosc_parametru WHERE id = NEW.wartosc_id);
SET @ID_param := (SELECT parametr_id from Wartosc_parametru WHERE id=@ID_wart); 
SET @ID_segm := (SELECT segment_id from Parametr_segmentu WHERE parametr_id = @ID_param);

IF @ID_segm <> (SELECT segment_id from Pozycja WHERE pozycja_id=NEW.pozycja_id AND faktura_id=NEW.faktura_id) THEN
SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Nieprawidlowy parametr dla danego segmentu';
END IF;
END;
//
DELIMITER ;
 
DROP TRIGGER IF EXISTS Status_faktury;

DELIMITER //
CREATE TRIGGER Status_faktury
AFTER UPDATE ON Pozycja FOR EACH ROW
BEGIN
 IF OLD.status<>NEW.status THEN
   IF (SELECT COUNT(*) FROM Pozycja WHERE faktura_id = NEW.faktura_id) = (SELECT COUNT(*) FROM Pozycja WHERE faktura_id = NEW.faktura_id AND status = NEW.status) THEN
     UPDATE Faktura SET status = NEW.status WHERE faktura_id = NEW.faktura_id;
   END IF;
 END IF;
END;
//
DELIMITER ;
