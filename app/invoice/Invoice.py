import os
import subprocess
import time
from math import floor
import random


class Invoice:
    def __init__(self, output_file='output.pdf'):
        # Load the data template
        with open('invoice_data_template.tex', 'r') as file:
            self.data = file.read()

        # Store the output file path
        self.output_file = output_file

        # initialize the invoice entries list
        self.entries = ""
        self.entries_sum_netto = 0
        self.entries_sum_vat = 0
        self.entries_sum_brutto = 0
        self.entries_count = 0

        # Set the invoice generation date as the current one
        self.setDateGenerated(time.strftime("%d.%m.%Y"))

    def __addInvoiceEntryStr(self, name, count, price_netto, vat_percents, price_vat, price_brutto):
        self.entries += "\invoiceline{" + name +\
                        "}{" + count +\
                        "}{" + price_netto +\
                        "}{" + vat_percents +\
                        "}{" + price_vat +\
                        "}{" + price_brutto +\
                        "}\n"

    def addInvoiceEntry(self, name, count, price_netto):
        p_netto = round(price_netto, 2)
        p_vat = round(p_netto*0.23, 2)
        p_brutto = round(p_netto + p_vat, 2)

        self.entries_sum_netto += p_netto
        self.entries_sum_vat += p_vat
        self.entries_sum_brutto += p_brutto
        self.entries_count += count

        self.__addInvoiceEntryStr(name, str(count), ("%.2f" % p_netto), "23", ("%.2f" % p_vat), ("%.2f" % p_brutto))

    def setBuyerPerson(self, name, surname, street, city, phone_number, pesel):
        self.data = self.data.replace("LINE1", name + " " + surname)
        self.data = self.data.replace("LINE2", street)
        self.data = self.data.replace("LINE3", city)
        self.data = self.data.replace("LINE4", "tel: " + phone_number)
        self.data = self.data.replace("LINE5", "PESEL: " + pesel)

    def setBuyerCompany(self, name, street, city, phone_number, nip):
        self.data = self.data.replace("LINE1", name)
        self.data = self.data.replace("LINE2", street)
        self.data = self.data.replace("LINE3", city)
        self.data = self.data.replace("LINE4", "tel: " + phone_number)
        self.data = self.data.replace("LINE5", "NIP: " + nip)

    def setID(self, id):
        self.data = self.data.replace("INVOICENUMBER", id)

    def setDateGenerated(self, date):
        self.data = self.data.replace("DATEINVOICE", date)

    def setDateSold(self, date):
        self.data = self.data.replace("DATESOLD", date)

    def setDatePayment(self, date):
        self.data = self.data.replace("DATEPAYMENT", date)

    def setSums(self):
        self.entries_sum_netto = round(self.entries_sum_netto, 2)
        self.entries_sum_vat = round(self.entries_sum_vat, 2)
        self.entries_sum_brutto = round(self.entries_sum_brutto, 2)

        self.data = self.data.replace("SUMCOUNTS", str(self.entries_count))
        self.data = self.data.replace("SUMNETTO", ("%.2f" % self.entries_sum_netto).replace(".", ","))
        self.data = self.data.replace("SUMVAT", ("%.2f" % self.entries_sum_vat).replace(".", ","))
        self.data = self.data.replace("SUMBRUTTO", ("%.2f" % self.entries_sum_brutto).replace(".", ","))

        self.data = self.data.replace("SUMTEXTZL", self.numberToText(floor(self.entries_sum_brutto)))
        textgr = self.__numToStr(round((self.entries_sum_brutto - int(self.entries_sum_brutto))*100.0))
        if textgr == '':
            textgr = "zero"
        self.data = self.data.replace("SUMTEXTGR", textgr)

    def numberToText(self, number):
        if number == 0:
            return "zero"

        output = ""
        UNITS = [[],
                 ["tysiąc", "tysiące", "tysięcy"],
                 ["milion", "miliony", "milionów"],
                 ["miliard", "miliardy", "miliardów"]]

        num = str(number)
        l = len(num)
        if l <= 3:
            return self.__numToStr(number)

        num = "0" * ((3 - l % 3) % 3) + num
        for i, j in enumerate(reversed(range(l // 3))):
            part = self.__numToStr(int(num[i * 3:(i + 1) * 3]))

            if j > 0:
                if part[-1] == "n":
                    unit = UNITS[j][0]
                elif part[-1] == 'y' or part[-2] == "wa":
                    unit = UNITS[j][1]
                else:
                    unit = UNITS[j][2]
                part += " " + unit

            output += part + " "

        return output.strip()

    def __numToStr(self, number):
        ONES = ["", "jeden", "dwa", "trzy", "cztery", "pięć", "sześć", "siedem", "osiem", "dziewięć"]
        DOZENS = ["dziesięć", "jedenaście", "dwanaście", "trzynaście", "czternaście", "piętnaście", "szesnaście",
                 "siedemnaście", "osiemnaście", "dziewiętnaście"]
        TENS = ["", "dziesięć", "dwadzieścia", "trzydzieści", "czterdzieści", "pięćdziesiąt", "sześćdziesiąt",
               "siedemdziesiąt", "osiemdziesiąt", "dziewięćdziesiąt"]
        HUNDREDS = ["", "sto", "dwieście", "trzysta", "czterysta", "pięćset", "sześćset", "siedemset", "osiemset",
                   "dziewięćset"]

        output = HUNDREDS[number // 100] + " "
        n100 = number % 100
        n10 = number % 10
        if n100 >= 20:
            output += TENS[n100 // 10] + " "
            output += ONES[n10]
        elif n100 >= 10:
            output += DOZENS[n100 - 10] + " "
        else:
            output += ONES[n10]

        return output.strip()

    def addDelivery(self, price_netto):
        price_netto = round(price_netto, 2)
        self.data = self.data.replace("DELIVERYNETTO", ("%.2f" % price_netto).replace(".", ","))
        price_vat = round(price_netto * 0.08, 2)
        price_brutto = round(price_netto + price_vat, 2)
        self.data = self.data.replace("DELIVERYVAT", ("%.2f" % price_vat).replace(".", ","))
        self.data = self.data.replace("DELIVERYBRUTTO", ("%.2f" % price_brutto).replace(".", ","))
        self.data = self.data.replace("DELIVERY", "1")
        self.entries_sum_brutto += price_brutto
        self.entries_sum_netto += price_netto
        self.entries_sum_vat += price_vat

    def addAssembly(self, price_netto):
        price_netto = round(price_netto, 2)
        self.data = self.data.replace("ASSEMBLYNETTO", ("%.2f" % price_netto).replace(".", ","))
        price_vat = round(price_netto * 0.08, 2)
        price_brutto = round(price_netto + price_vat, 2)
        self.data = self.data.replace("ASSEMBLYVAT", ("%.2f" % price_vat).replace(".", ","))
        self.data = self.data.replace("ASSEMBLYBRUTTO", ("%.2f" % price_brutto).replace(".", ","))
        self.data = self.data.replace("ASSEMBLY", "1")
        self.entries_sum_brutto += price_brutto
        self.entries_sum_netto += price_netto
        self.entries_sum_vat += price_vat

    def generate(self):
        # Set the invoice total sums
        self.setSums()

        # Store the invoice entries
        self.data = self.data.replace("INVOICELINES", self.entries.replace(".", ","))

        # Prepare the data file
        with open('invoice_data.tex', 'w') as file:
            file.write(self.data)

        # Generate the output file
        for i in range(10):
            print("PDFLaTeX running...")
            out, err = subprocess.Popen("pdflatex -synctex=1 -interaction=nonstopmode invoice_template.tex", stdout=subprocess.PIPE, shell=True).communicate()
            if b"Rerun" not in out:
                break

        # Cleanup
        os.rename("invoice_template.pdf", self.output_file)
        os.remove("invoice_data.tex")
        os.remove("invoice_template.aux")
        os.remove("invoice_template.log")
        os.remove("invoice_template.synctex.gz")

    def open(self):
        os.system("xdg-open " + self.output_file)


if __name__ == "__main__":
    inv = Invoice()
    inv.setID("FV/2017/06/123456")
    inv.setDateSold("09.07.2017")
    inv.setDatePayment("10.07.2017")
    inv.setBuyerCompany("Wydział Mechaniczny Energetyki i Lotnictwa", "ul. Nowowiejska 24", "00-001 Warszawa", "22 234 73 54", "525-000-58-34")
    # inv.setBuyerPerson("Jan", "Kowalski", "ul. Długa 12/3", "02-678 Warszawa", "601 503 402", "94010203456")
    inv.addInvoiceEntry("Segment 1", 1, 1.00)
    inv.addInvoiceEntry("Segment 2", 2, 13.00)
    inv.addInvoiceEntry("Segment 3", 1, 11.5123123123)
    inv.addInvoiceEntry("Segment 4", 4, 121.12445)
    inv.addInvoiceEntry("Segment 5", 10, 130.0)
    inv.addDelivery(100.0)
    inv.addAssembly(200.0)
    inv.generate()
    inv.open()