import datetime


stawka_vat_procent = 23
stawka_dzierżawy = 2.00
data_start = '10.09.2021'
data_stop = '31.12.2022'
powierzchnia_dzierżawy = 195.0


data_start_obj = datetime.datetime.strptime(data_start, '%d.%m.%Y')
data_stop_obj = datetime.datetime.strptime(data_stop, '%d.%m.%Y')
czas_dzierżawy_dni = (data_stop_obj - data_start_obj).days + 1
czynsz_netto = stawka_dzierżawy * powierzchnia_dzierżawy * czas_dzierżawy_dni
czynsz_vat = czynsz_netto * stawka_vat_procent / 100
czynsz_brutto = czynsz_netto + czynsz_vat

print('stawka_vat_procent = ' + str(stawka_vat_procent))
print('stawka_dzierżawy = ' + '{:0.2f}'.format(stawka_dzierżawy).replace('.', ','))
print('data_start = ' + data_start)
print('data_stop = ' + data_stop)
print('czas_dzierżawy_dni = ' + str(czas_dzierżawy_dni))
print('powierzchnia_dzierżawy = ' + str(powierzchnia_dzierżawy).replace('.', ','))
print('czynsz_netto = ' + '{:0.2f}'.format(czynsz_netto).replace('.', ','))
print('czynsz_vat = ' + '{:0.2f}'.format(czynsz_vat).replace('.', ','))
print('czynsz_brutto = ' + '{:0.2f}'.format(czynsz_brutto).replace('.', ','))
