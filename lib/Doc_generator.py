SCRIPT_NAME = 'Doc_generator'
SCRIPT_VERSION = '3.4'
GENERAL_INFO = u"""
author: Piotr Michałowski, Olsztyn, woj. W-M, Poland
email: piotrm35@hotmail.com
work begin: 12.07.2021
description: Generator dokumentów oparty na szablonach i plikach kongiguracyjnych.
"""

# Uwaga: należy pamiętać, że wstawiając znaczniki do szablonów trzeba je wstawiać w całości (razem z []), bo w przeciwnym przypadku nie będzie działć wyszukiwanie (DOCX runs oddzieli [] na początku i na końcu).

import os, datetime
from docx import Document                   # sudo pip3 install python-docx
try:
    from lib.Liczebniki import get_liczebnik_dtct
except:
    from Liczebniki import get_liczebnik_dtct

#====================================================================================================================


class Doc_generator:


    KLAUZULA_REKOMPENSATY = '\nW przypadku opóźnień w zapłacie czynszu, pobierana będzie zryczałtowana rekompensata za koszty odzyskiwania należności w wysokości nie niższej niż 40 euro (w przeliczeniu na złotówki), bez wezwania, która przysługuje od dnia, w którym świadczenie pieniężne stało się wymagalne.'


    TEMPLATES = {
        'awaria_roboty.docx':
            [
                '+[DATA_DZISIEJSZA]',           # jeśli znacznik zaczyna się od znaku "+", to nie jest brany pod uwagę przy sprawdzaniu zgodności znaczników między plikiem konfiguracyjnym i tą listą (jest w szablonie ale nie ma go w pliku konfiguracyjnym)
                '[NR_SPRAWY]',
                '[ADRES_STRONY]',
                '[DATA_ZAWIADOMIENIE]',
                '[DATA_START_BEZUMOWNE]',
                '[DATA_STOP_BEZUMOWNE]',
                '[DZIAŁKI_DO_ZAJĘCIA]',
                '[POWIERZCHNIA_M2]',
                '[STAWKA_CZYNSZU_NETTO]',
                '[STAWKA_CZYNSZU_OKRES]',       # -> musi być w pliku konfiguracyjnym ale nie może być w szablonie
                '[STAWKA_VAT_PROCENT]'
                #'[CZAS_ZAJĘCIA_DNI]', -> wypełniana automatycznie (czyli musi być w szablonie ale nie może być w pliku konfiguracyjnym)
                #'[STAWKA_VAT_LICZBA]', -> wypełniana automatycznie (czyli musi być w szablonie ale nie może być w pliku konfiguracyjnym)
                #'[CZYNSZ_NETTO_LICZBA_ROBOTY]', -> wypełniana automatycznie (czyli musi być w szablonie ale nie może być w pliku konfiguracyjnym)
                #'[VAT_LICZBA_ROBOTY]', -> wypełniana automatycznie (czyli musi być w szablonie ale nie może być w pliku konfiguracyjnym)
                #'[CZYNSZ_BRUTTO_LICZBA_ROBOTY]' -> wypełniana automatycznie (czyli musi być w szablonie ale nie może być w pliku konfiguracyjnym)
            ],
        'bezumowne_korzystanie_ZP_roboty.docx':
            [
                '+[DATA_DZISIEJSZA]',           # jeśli znacznik zaczyna się od znaku "+", to nie jest brany pod uwagę przy sprawdzaniu zgodności znaczników między plikiem konfiguracyjnym i tą listą (jest w szablonie ale nie ma go w pliku konfiguracyjnym)
                '[NR_SPRAWY]',
                '[ADRES_STRONY]',
                '[DATA_ZAWIADOMIENIE]',
                '[DATA_START_BEZUMOWNE]',
                '[DATA_STOP_BEZUMOWNE]',
                '[DZIAŁKI_DO_ZAJĘCIA]',
                '[POWIERZCHNIA_M2]',
                '[STAWKA_CZYNSZU_NETTO]',
                '[STAWKA_CZYNSZU_OKRES]',       # -> musi być w pliku konfiguracyjnym ale nie może być w szablonie
                '[STAWKA_VAT_PROCENT]'
                #'[CZAS_ZAJĘCIA_DNI]', -> wypełniana automatycznie (czyli musi być w szablonie ale nie może być w pliku konfiguracyjnym)
                #'[STAWKA_VAT_LICZBA]', -> wypełniana automatycznie (czyli musi być w szablonie ale nie może być w pliku konfiguracyjnym)
                #'[CZYNSZ_NETTO_LICZBA_ROBOTY]', -> wypełniana automatycznie (czyli musi być w szablonie ale nie może być w pliku konfiguracyjnym)
                #'[VAT_LICZBA_ROBOTY]', -> wypełniana automatycznie (czyli musi być w szablonie ale nie może być w pliku konfiguracyjnym)
                #'[CZYNSZ_BRUTTO_LICZBA_ROBOTY]' -> wypełniana automatycznie (czyli musi być w szablonie ale nie może być w pliku konfiguracyjnym)
            ],
        'umowa_dzierżawa_roboty.docx': 
            [
                '[NR_SPRAWY]',
                '[ZDZIT_REPREZENTACJA]',
                '[NAZWA_STRONY]',
                '[NIP_REGON_KRS]',
                '[REPREZENTACJA_STRONY]',
                '[ZWANYM_RODZAJ]',
                '[NAZWA_ULICY]',
                '[DZIAŁKI_DO_ZAJĘCIA]',
                '[POWIERZCHNIA_M2]',
                '[W_CELU_WYBUDOWANIA_UMIESZCZENIA]',
                '[NIEZWIĄZANEGO_RODZAJ]',
                '[CZAS_ZAJĘCIA_DNI]',           # -> musi być w pliku konfiguracyjnym ale nie może być w szablonie
                '[UMOWA_ZOSTAJE_ZAWARTA_NA_CZAS]',
                '[STAWKA_CZYNSZU_NETTO]',
                '[STAWKA_CZYNSZU_OKRES]',       # -> musi być w pliku konfiguracyjnym ale nie może być w szablonie
                '[STAWKA_VAT_PROCENT]'
                #'[CZYNSZ_BRUTTO_LICZBA_ROBOTY]', -> wypełniana automatycznie (czyli musi być w szablonie ale nie może być w pliku konfiguracyjnym)
                #'[CZYNSZ_BRUTTO_SŁOWNIE_ROBOTY]', -> wypełniana automatycznie (czyli musi być w szablonie ale nie może być w pliku konfiguracyjnym)
                #'[VAT_LICZBA_ROBOTY]', -> wypełniana automatycznie (czyli musi być w szablonie ale nie może być w pliku konfiguracyjnym)
                #'[VAT_SŁOWNIE_ROBOTY]', -> wypełniana automatycznie (czyli musi być w szablonie ale nie może być w pliku konfiguracyjnym)
                #'[K1LAUZULA_REKOMPENSATY]' -> wypełniana automatycznie (czyli musi być w szablonie ale nie może być w pliku konfiguracyjnym)
            ],
        'protokół_przekazania_terenu_dzierżawa_roboty.docx':
             [
                '[DZIAŁKI_DO_ZAJĘCIA]',
                '[POWIERZCHNIA_M2]',
                '[W_CELU_WYBUDOWANIA_UMIESZCZENIA]',
                '[ADRES_STRONY]',
                '[NR_SPRAWY]'
            ],
        'zawiadomienie_do_Prezydenta_dzierżawa_roboty.docx':
            [
                '+[DATA_DZISIEJSZA]',           # jeśli znacznik zaczyna się od znaku "+", to nie jest brany pod uwagę przy sprawdzaniu zgodności znaczników między plikiem konfiguracyjnym i tą listą (jest w szablonie ale nie ma go w pliku konfiguracyjnym)
                '+[NUMER_PISMA]',               # jeśli znacznik zaczyna się od znaku "+", to nie jest brany pod uwagę przy sprawdzaniu zgodności znaczników między plikiem konfiguracyjnym i tą listą (jest w szablonie ale nie ma go w pliku konfiguracyjnym)
                '[NAZWA_STRONY]',
                '[DZIAŁKI_DO_ZAJĘCIA]',
                '[NR_SPRAWY]'
            ],
        'umowa_dzierżawa_umieszczenie.docx':
            [
                '[NR_SPRAWY]',
                '[ZDZIT_REPREZENTACJA]',
                '[NAZWA_STRONY]',
                '[NIP_REGON_KRS]',
                '[REPREZENTACJA_STRONY]',
                '[ZWANYM_RODZAJ]',
                '[NAZWA_ULICY]',
                '[DZIAŁKI_DO_ZAJĘCIA]',
                '[POWIERZCHNIA_M2]',
                '[UDZIAL_JEDEN_NA]',
                '[W_CELU_WYBUDOWANIA_UMIESZCZENIA]',
                '[NIEZWIĄZANEGO_RODZAJ]',
                '[UMOWA_ZOSTAJE_ZAWARTA_NA_CZAS]',
                '[STAWKA_CZYNSZU_NETTO]',
                '[STAWKA_CZYNSZU_OKRES]',       # -> musi być w pliku konfiguracyjnym ale nie może być w szablonie
                '[STAWKA_VAT_PROCENT]'
                #'[ROK_AKTUALNY]', -> wypełniana automatycznie (czyli musi być w szablonie ale nie może być w pliku konfiguracyjnym)
                #'[ROK_KOLEJNY]', -> wypełniana automatycznie (czyli musi być w szablonie ale nie może być w pliku konfiguracyjnym)
                #'[CZYNSZ_BRUTTO_LICZBA_UMIESZCZENIE]', -> wypełniana automatycznie (czyli musi być w szablonie ale nie może być w pliku konfiguracyjnym)
                #'[CZYNSZ_BRUTTO_SŁOWNIE_UMIESZCZENIE]', -> wypełniana automatycznie (czyli musi być w szablonie ale nie może być w pliku konfiguracyjnym)
                #'[K1LAUZULA_REKOMPENSATY]' -> wypełniana automatycznie (czyli musi być w szablonie ale nie może być w pliku konfiguracyjnym)
            ],
        'protokół_przekazania_terenu_dzierżawa_umieszczenie.docx':
            [
                '[DZIAŁKI_DO_ZAJĘCIA]',
                '[POWIERZCHNIA_M2]',
                '[UDZIAL_JEDEN_NA]',
                '[W_CELU_WYBUDOWANIA_UMIESZCZENIA]',
                '[ADRES_STRONY]',
                '[NR_SPRAWY]'
            ],
        'wniosek_na_kolegium_Prezydenta_dzierżawa_umieszczenie.docx':
            [
                '+[DATA_DZISIEJSZA]',           # jeśli znacznik zaczyna się od znaku "+", to nie jest brany pod uwagę przy sprawdzaniu zgodności znaczników między plikiem konfiguracyjnym i tą listą (jest w szablonie ale nie ma go w pliku konfiguracyjnym)
                '[DZIAŁKI_DO_ZAJĘCIA]',
                '[NAZWA_ULICY]',
                '[NAZWA_STRONY]',
                '[NIP_REGON_KRS]',
                '[UMOWA_ZOSTAJE_ZAWARTA_NA_CZAS]',
                '[W_CELU_WYBUDOWANIA_UMIESZCZENIA]',
                '[NR_SPRAWY]'
            ],
        'zawiadomienie_do_Prezydenta_dzierżawa_umieszczenie.docx':
            [
                '+[DATA_DZISIEJSZA]',           # jeśli znacznik zaczyna się od znaku "+", to nie jest brany pod uwagę przy sprawdzaniu zgodności znaczników między plikiem konfiguracyjnym i tą listą (jest w szablonie ale nie ma go w pliku konfiguracyjnym)
                '+[NUMER_PISMA]',               # jeśli znacznik zaczyna się od znaku "+", to nie jest brany pod uwagę przy sprawdzaniu zgodności znaczników między plikiem konfiguracyjnym i tą listą (jest w szablonie ale nie ma go w pliku konfiguracyjnym)
                '[NAZWA_STRONY]',
                '[DZIAŁKI_DO_ZAJĘCIA]',
                '[NR_SPRAWY]'
            ],
        'przekazanie_umowy_na_umieszczenie_do_podpisu.docx':
            [
                '+[DATA_DZISIEJSZA]',           # jeśli znacznik zaczyna się od znaku "+", to nie jest brany pod uwagę przy sprawdzaniu zgodności znaczników między plikiem konfiguracyjnym i tą listą (jest w szablonie ale nie ma go w pliku konfiguracyjnym)
                '+[NUMER_PISMA]',               # jeśli znacznik zaczyna się od znaku "+", to nie jest brany pod uwagę przy sprawdzaniu zgodności znaczników między plikiem konfiguracyjnym i tą listą (jest w szablonie ale nie ma go w pliku konfiguracyjnym)
                '[ADRES_STRONY]',
                '[DZIAŁKI_DO_ZAJĘCIA]',
                '[W_CELU_WYBUDOWANIA_UMIESZCZENIA]',
                '[NR_SPRAWY]'
            ],
        'bezumowne_korzystanie_ZP_umieszczenie.docx':
            [
                '+[DATA_DZISIEJSZA]',           # jeśli znacznik zaczyna się od znaku "+", to nie jest brany pod uwagę przy sprawdzaniu zgodności znaczników między plikiem konfiguracyjnym i tą listą (jest w szablonie ale nie ma go w pliku konfiguracyjnym)
                '+[NUMER_PISMA]',               # jeśli znacznik zaczyna się od znaku "+", to nie jest brany pod uwagę przy sprawdzaniu zgodności znaczników między plikiem konfiguracyjnym i tą listą (jest w szablonie ale nie ma go w pliku konfiguracyjnym)
                '+[MIANOWNIK]',                 # jeśli znacznik zaczyna się od znaku "+", to nie jest brany pod uwagę przy sprawdzaniu zgodności znaczników między plikiem konfiguracyjnym i tą listą (jest w szablonie ale nie ma go w pliku konfiguracyjnym)
                '[ADRES_STRONY]',
                '[DATA_START_BEZUMOWNE]',
                '[DATA_STOP_BEZUMOWNE]',
                '[DZIAŁKI_DO_ZAJĘCIA]',
                '[POWIERZCHNIA_M2]',
                '[UDZIAL_JEDEN_NA]',
                '[STAWKA_CZYNSZU_NETTO]',
                '[STAWKA_CZYNSZU_OKRES]',       # -> musi być w pliku konfiguracyjnym ale nie może być w szablonie
                '[STAWKA_VAT_PROCENT]'
                #'[CZAS_DNI_BEZUMOWNE_UMIESZCZENIE]', -> wypełniana automatycznie (czyli musi być w szablonie ale nie może być w pliku konfiguracyjnym)
                #'[STAWKA_VAT_LICZBA]', -> wypełniana automatycznie (czyli musi być w szablonie ale nie może być w pliku konfiguracyjnym)
                #'[CZYNSZ_NETTO_LICZBA_UMIESZCZENIE]', -> wypełniana automatycznie (czyli musi być w szablonie ale nie może być w pliku konfiguracyjnym)
                #'[VAT_LICZBA_UMIESZCZENIE]', -> wypełniana automatycznie (czyli musi być w szablonie ale nie może być w pliku konfiguracyjnym)
                #'[CZYNSZ_BRUTTO_LICZBA_UMIESZCZENIE]' -> wypełniana automatycznie (czyli musi być w szablonie ale nie może być w pliku konfiguracyjnym)
            ],
        'ANEKS_nr_1_do_umowy_dzierżawy_umieszczenie_czas_nieokreślony.docx':
            [
                '[NR_SPRAWY]',
                '[DATA_ZAWARCIA_UMOWY]',
                '[NAZWA_STRONY]',
                '[NAZWA_ULICY]',
                '[DZIAŁKI_DO_ZAJĘCIA]',
                '[POWIERZCHNIA_M2]',
                '[UDZIAL_JEDEN_NA]',
                '[W_CELU_WYBUDOWANIA_UMIESZCZENIA]',
                '[ZDZIT_REPREZENTACJA]',
                '[NAZWA_STRONY]',
                '[NIP_REGON_KRS]',
                '[REPREZENTACJA_STRONY]',
                '[ZWANYM_RODZAJ]',
                '[UMOWA_ZOSTAJE_ZAWARTA_NA_CZAS]',
                '[STAWKA_CZYNSZU_NETTO]',
                '[STAWKA_CZYNSZU_OKRES]',      # -> musi być w pliku konfiguracyjnym ale nie może być w szablonie
                '[STAWKA_VAT_PROCENT]'
                #'[ROK_AKTUALNY]', -> wypełniana automatycznie (czyli musi być w szablonie ale nie może być w pliku konfiguracyjnym)
                #'[ROK_KOLEJNY]', -> wypełniana automatycznie (czyli musi być w szablonie ale nie może być w pliku konfiguracyjnym)
                #'[CZYNSZ_BRUTTO_LICZBA_UMIESZCZENIE]', -> wypełniana automatycznie (czyli musi być w szablonie ale nie może być w pliku konfiguracyjnym)
                #'[CZYNSZ_BRUTTO_SŁOWNIE_UMIESZCZENIE]', -> wypełniana automatycznie (czyli musi być w szablonie ale nie może być w pliku konfiguracyjnym)
                #'[K1LAUZULA_REKOMPENSATY]' -> wypełniana automatycznie (czyli musi być w szablonie ale nie może być w pliku konfiguracyjnym)
            ]
        }


    def make_doc_by_config_file_path(self, template_file_name, config_file_path):
        dane_sprawy_dict = self.get_config_dict_from_file(config_file_path)
        return self.make_doc_by_dictionary(template_file_name, dane_sprawy_dict, config_file_path)


    def make_doc_by_dictionary(self, template_file_name, dane_sprawy_dict, config_file_path):
        if self.is_subset_of_list(self.TEMPLATES[template_file_name], list(dane_sprawy_dict.keys())):
            doc = Document(os.path.join('dane', template_file_name))
            for key in self.TEMPLATES[template_file_name]:
                if key == '+[DATA_DZISIEJSZA]':
                    self.replace_text_DOCX(doc, key, self.get_time_str())
                elif key == '+[NUMER_PISMA]':
                    nr_sprawy = self.get_string_from_config(dane_sprawy_dict, '[NR_SPRAWY]')
                    nr_sprawy_list = nr_sprawy.split('.')
                    nr_pisma = nr_sprawy_list[0] + '.' + nr_sprawy_list[1] + '.' + nr_sprawy_list[2] + '-.....' + nr_sprawy_list[3]
                    self.replace_text_DOCX(doc, key, nr_pisma)
                elif key == '+[MIANOWNIK]':
                    udzial_jeden_na = self.get_string_from_config(dane_sprawy_dict, '[UDZIAL_JEDEN_NA]')
                    if udzial_jeden_na and self.is_int(udzial_jeden_na):
                        udzial_jeden_na_int = int(udzial_jeden_na)
                        if udzial_jeden_na_int > 1:
                            self.replace_text_DOCX(doc, key, '(365 * ' + str(udzial_jeden_na) + ')')
                        else:
                            self.replace_text_DOCX(doc, key, '365')
                    else:
                        self.replace_text_DOCX(doc, key, '365')
                elif key == '[NIP_REGON_KRS]':
                    nip_regon_krs = self.get_string_from_config(dane_sprawy_dict, key)
                    if not nip_regon_krs.startswith(', '):
                        nip_regon_krs = ', ' + nip_regon_krs
                    self.replace_text_DOCX(doc, key, nip_regon_krs)
                elif key == '[ADRES_STRONY]':
                    if template_file_name in ['awaria_roboty.docx', 'bezumowne_korzystanie_ZP_roboty.docx', 'zawiadomienie_do_Prezydenta_dzierżawa_roboty.docx', 'zawiadomienie_do_Prezydenta_dzierżawa_umieszczenie.docx', 'przekazanie_umowy_na_umieszczenie_do_podpisu.docx', 'bezumowne_korzystanie_ZP_umieszczenie.docx']:
                        new_text = self.get_string_from_config(dane_sprawy_dict, key)
                        new_text = new_text.replace(', ', '\n')
                        self.replace_text_DOCX(doc, key, new_text)
                    else:
                        self.replace_key_from_config_DOCX(doc, dane_sprawy_dict, key)
                elif key in ['[CZAS_ZAJĘCIA_DNI]', '[STAWKA_CZYNSZU_OKRES]']:
                    pass
                elif key == '[UDZIAL_JEDEN_NA]':
                    udzial_jeden_na = self.get_string_from_config(dane_sprawy_dict, key)
                    if udzial_jeden_na and self.is_int(udzial_jeden_na):
                        print('udzial_jeden_na = ' + str(udzial_jeden_na))
                        udzial_jeden_na_int = int(udzial_jeden_na)
                        if udzial_jeden_na_int > 1:
                            self.replace_text_DOCX(doc, key, ' (udział 1/' + str(udzial_jeden_na) + ') ')
                        else:
                            self.replace_text_DOCX(doc, key, '')
                    else:
                        self.replace_text_DOCX(doc, key, '')
                elif key == '[STAWKA_CZYNSZU_NETTO]':
                    stawka_vat_procent = self.get_string_from_config(dane_sprawy_dict, '[STAWKA_VAT_PROCENT]')
                    stawka_vat_procent = float(stawka_vat_procent.replace(',', '.'))
                    stawka_dzierżawy_str = self.get_string_from_config(dane_sprawy_dict, '[STAWKA_CZYNSZU_NETTO]')
                    print('stawka_dzierżawy_str = ' + str(stawka_dzierżawy_str))
                    stawka_dzierżawy = float(stawka_dzierżawy_str.replace(',', '.'))
                    powierzchnia_dzierżawy = self.get_string_from_config(dane_sprawy_dict, '[POWIERZCHNIA_M2]')
                    powierzchnia_dzierżawy = float(powierzchnia_dzierżawy.replace(',', '.'))
                    stawka_czynszu_okres = self.get_string_from_config(dane_sprawy_dict, '[STAWKA_CZYNSZU_OKRES]')
                    if stawka_czynszu_okres == 'dzienna':   # umowa_dzierżawa_roboty.docx lub bezumowne_korzystanie_ZP_roboty.docx lub awaria_roboty.docx
                        if template_file_name == 'umowa_dzierżawa_roboty.docx':
                            czas_dzierżawy = self.get_string_from_config(dane_sprawy_dict, '[CZAS_ZAJĘCIA_DNI]')
                            czas_dzierżawy = float(czas_dzierżawy.replace(',', '.'))
                        else:
                            data_start = self.get_string_from_config(dane_sprawy_dict, '[DATA_START_BEZUMOWNE]')
                            data_stop = self.get_string_from_config(dane_sprawy_dict, '[DATA_STOP_BEZUMOWNE]')
                            data_start_obj = datetime.datetime.strptime(data_start, '%d.%m.%Y')
                            data_stop_obj = datetime.datetime.strptime(data_stop, '%d.%m.%Y')
                            czas_dzierżawy = (data_stop_obj - data_start_obj).days + 1
                            self.replace_text_DOCX(doc, '[CZAS_ZAJĘCIA_DNI]', czas_dzierżawy)
                        czynsz_netto = stawka_dzierżawy * powierzchnia_dzierżawy * czas_dzierżawy
                        czynsz_vat = stawka_vat_procent * czynsz_netto / 100
                        czynsz_brutto = czynsz_netto + czynsz_vat
                        czynsz_brutto_dict = get_liczebnik_dtct(czynsz_brutto)
                        czynsz_vat_dict = get_liczebnik_dtct(czynsz_vat)
                        self.replace_text_DOCX(doc, '[CZYNSZ_BRUTTO_LICZBA_ROBOTY]', czynsz_brutto_dict['liczba'])
                        self.replace_text_DOCX(doc, '[VAT_LICZBA_ROBOTY]', czynsz_vat_dict['liczba'])
                        if template_file_name == 'umowa_dzierżawa_roboty.docx':
                            self.replace_text_DOCX(doc, '[CZYNSZ_BRUTTO_SŁOWNIE_ROBOTY]', czynsz_brutto_dict['liczebnik'])
                            self.replace_text_DOCX(doc, '[VAT_SŁOWNIE_ROBOTY]', czynsz_vat_dict['liczebnik'])
                            if czynsz_brutto >= 100:
                                self.replace_text_DOCX(doc, '[K1LAUZULA_REKOMPENSATY]', self.KLAUZULA_REKOMPENSATY)
                            else:
                                self.replace_text_DOCX(doc, '[K1LAUZULA_REKOMPENSATY]', '')
                        else:
                            czynsz_netto_dict = get_liczebnik_dtct(czynsz_netto)
                            self.replace_text_DOCX(doc, '[CZYNSZ_NETTO_LICZBA_ROBOTY]', czynsz_netto_dict['liczba'])
                            self.replace_text_DOCX(doc, '[STAWKA_VAT_LICZBA]', stawka_vat_procent / 100)
                    elif stawka_czynszu_okres == 'roczna':  # umowa_dzierżawa_umieszczenie.docx lub bezumowne_korzystanie_ZP_umieszczenie.docx lub ANEKS_nr_1_do_umowy_dzierżawy_umieszczenie_czas_nieokreślony.docx
                        udzial_jeden_na = self.get_string_from_config(dane_sprawy_dict, '[UDZIAL_JEDEN_NA]')
                        if udzial_jeden_na and self.is_int(udzial_jeden_na):
                            udzial_jeden_na_int = int(udzial_jeden_na)
                            if udzial_jeden_na_int < 1:
                                print('???? -> udzial_jeden_na_int = ' + str(udzial_jeden_na_int))
                                return
                        else:
                            udzial_jeden_na_int = 1
                        if template_file_name == 'umowa_dzierżawa_umieszczenie.docx' or template_file_name == 'ANEKS_nr_1_do_umowy_dzierżawy_umieszczenie_czas_nieokreślony.docx':
                            czas_dzierżawy = 1  # rok
                            czynsz_netto = stawka_dzierżawy * powierzchnia_dzierżawy * czas_dzierżawy / udzial_jeden_na_int
                            czynsz_vat = stawka_vat_procent * czynsz_netto / 100
                            czynsz_brutto = czynsz_netto + czynsz_vat
                            czynsz_brutto_dict = get_liczebnik_dtct(czynsz_brutto)
                            self.replace_text_DOCX(doc, '[CZYNSZ_BRUTTO_LICZBA_UMIESZCZENIE]', czynsz_brutto_dict['liczba'])
                            self.replace_text_DOCX(doc, '[CZYNSZ_BRUTTO_SŁOWNIE_UMIESZCZENIE]', czynsz_brutto_dict['liczebnik'])
                            if czynsz_brutto >= 100:
                                self.replace_text_DOCX(doc, '[K1LAUZULA_REKOMPENSATY]', self.KLAUZULA_REKOMPENSATY)
                            else:
                                self.replace_text_DOCX(doc, '[K1LAUZULA_REKOMPENSATY]', '')
                            nr_sprawy = self.get_string_from_config(dane_sprawy_dict, '[NR_SPRAWY]')
                            rok_aktualny = int(nr_sprawy.split('.')[-1])
                            self.replace_text_DOCX(doc, '[ROK_AKTUALNY]', str(rok_aktualny))
                            self.replace_text_DOCX(doc, '[ROK_KOLEJNY]', str(rok_aktualny + 1))
                        elif template_file_name == 'bezumowne_korzystanie_ZP_umieszczenie.docx':
                            DATA_START_BEZUMOWNE = self.get_string_from_config(dane_sprawy_dict, '[DATA_START_BEZUMOWNE]')
                            DATA_STOP_BEZUMOWNE = self.get_string_from_config(dane_sprawy_dict, '[DATA_STOP_BEZUMOWNE]')
                            data_start_obj = datetime.datetime.strptime(DATA_START_BEZUMOWNE, '%d.%m.%Y')
                            data_stop_obj = datetime.datetime.strptime(DATA_STOP_BEZUMOWNE, '%d.%m.%Y')
                            czas_dzierżawy_dni = (data_stop_obj - data_start_obj).days + 1
                            czynsz_netto = stawka_dzierżawy * powierzchnia_dzierżawy * czas_dzierżawy_dni / (365 * udzial_jeden_na_int)
                            czynsz_vat = stawka_vat_procent * czynsz_netto / 100
                            czynsz_brutto = czynsz_netto + czynsz_vat
                            self.replace_text_DOCX(doc, '[CZAS_DNI_BEZUMOWNE_UMIESZCZENIE]', str(czas_dzierżawy_dni))
                            self.replace_text_DOCX(doc, '[STAWKA_VAT_LICZBA]', '{:0.2f}'.format(stawka_vat_procent / 100).replace('.', ','))
                            self.replace_text_DOCX(doc, '[CZYNSZ_NETTO_LICZBA_UMIESZCZENIE]', '{:0.2f}'.format(czynsz_netto).replace('.', ','))
                            self.replace_text_DOCX(doc, '[VAT_LICZBA_UMIESZCZENIE]', '{:0.2f}'.format(czynsz_vat).replace('.', ','))
                            self.replace_text_DOCX(doc, '[CZYNSZ_BRUTTO_LICZBA_UMIESZCZENIE]', '{:0.2f}'.format(czynsz_brutto).replace('.', ','))
                        else:
                            print('Doc_generator ERROR([STAWKA_CZYNSZU_NETTO]): template_file_name = ' + str(template_file_name))
                    else:
                        print('Doc_generator ERROR([STAWKA_CZYNSZU_NETTO]): stawka_czynszu_okres = ' + str(stawka_czynszu_okres))
                    self.replace_text_DOCX(doc, key, stawka_dzierżawy_str)
                else:
                    self.replace_key_from_config_DOCX(doc, dane_sprawy_dict, key)
            return self.save_document(dane_sprawy_dict, config_file_path, template_file_name, doc)
        else:
            print('Doc_generator: self.is_subset_of_list(self.TEMPLATES[template_file_name], dane_sprawy_dict.keys()) == False')
            return None


#----------------------------------------------------------------------------------------------------------------
# aux methods:


    def save_document(self, dane_sprawy_dict, config_file_path, template_file_name, doc):
        nr_sprawy = self.get_string_from_config(dane_sprawy_dict, '[NR_SPRAWY]')
        if nr_sprawy is None:
            nr_sprawy = self.get_string_from_config(dane_sprawy_dict, '[NR_SPRAWY]')
        nr_sprawy_list = nr_sprawy.split('.')
        nazwa_ulicy = self.get_string_from_config(dane_sprawy_dict, '[NAZWA_ULICY]')
        if len(nazwa_ulicy) > 20:
            nazwa_ulicy = nazwa_ulicy[0:20]
        nazwa_pliku_wynikowego = nr_sprawy_list[2] + '_' + template_file_name.replace('.docx', '') + '_' + nazwa_ulicy + '.docx'
        result_config_file_path = os.path.join(os.path.dirname(config_file_path), nazwa_pliku_wynikowego)
        doc.save(result_config_file_path)
        return nazwa_pliku_wynikowego
                      

    def get_config_dict_from_file(self, config_file_path):
        print('Doc_generator: get_config_dict_from_file - config_file_path: ' + str(config_file_path))
        try:
            config_file = open(config_file_path, 'r')
            config_text = config_file.read()
        except:
            config_file = open(config_file_path, mode='r', encoding='utf-8')
            config_text = config_file.read()
        config_file.close()
        config_text_list = [t for t in config_text.split('\n') if t and not t.startswith('#')]
        config_text_dict = {}
        for conf_tx in config_text_list:
            conf_tx = conf_tx.split('#')[0].strip()
            conf_tx_list = conf_tx.split(']:')
            if len(conf_tx_list) == 2:
                config_text_dict[(conf_tx_list[0] + ']').strip()] = conf_tx_list[1].strip()
            elif len(conf_tx_list) == 1:
                config_text_dict[(conf_tx_list[0] + ']').strip()] = ''
        print('Doc_generator: get_config_dict_from_file - config_text_dict: ' + str(config_text_dict))
        print('Doc_generator: get_config_dict_from_file - len(config_text_dict): ' + str(len(config_text_dict)))
        print('\n')
        return config_text_dict


    def replace_key_from_config_DOCX(self, doc, config_dict, key):
        new_text = self.get_string_from_config(config_dict, key)
        self.replace_text_DOCX(doc, key, new_text)


    def replace_text_DOCX(self, doc, old_tx, new_tx):
        print('Doc_generator replace_text_DOCX: ' + str(old_tx) + ' -> ' + str(new_tx))
        found = False
        for p in doc.paragraphs:
            if old_tx in p.text:
                inline = p.runs
                for i in range(len(inline)):
                    if old_tx in inline[i].text:
                        inline[i].text = inline[i].text.replace(old_tx, str(new_tx))
                        found = True
        if not found:
            print('Doc_generator replace_text_DOCX: ' + old_tx + ' NOT FOUND')


    def get_string_from_config(self, config_dict, key):
        if key in config_dict.keys():
            return config_dict[key].strip()
        else:
            print("Doc_generator get_string_from_config ERROR: there is no given key: " + key)
            return None


    def get_time_str(self):
        return str(datetime.datetime.now().strftime('%d.%m.%Y'))


    def is_subset_of_list(self, list_1, list_2):
        for el in list_1:
            if not el.startswith('+'):
                if el not in list_2:
                    print('Doc_generator is_subset_of_list is False: el = ' + str(el))
                    return False
        return True


    def is_int(self, x):
        try:
            f_x = int(x)
            return True
        except:
            return False


    def get_name(self):
        return SCRIPT_NAME +  ' ' + SCRIPT_VERSION


#====================================================================================================================


