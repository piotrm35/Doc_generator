# v. 0.2
    
jedności = ['zero ', 'jeden ', 'dwa ', 'trzy ', 'cztery ', 'pięć ', 'sześć ', 'siedem ', 'osiem ', 'dziewięć ']
naście = ['dziesięć ', 'jedenaście ', 'dwanaście ', 'trzynaście ', 'czternaście ', 'piętnaście ', 'szesnaście ', 'siedemnaście ', 'osiemnaście ', 'dziewiętnaście ']
dziesiątki = ['', 'dziesięć ', 'dwadzieścia ', 'trzydzieści ', 'czterdzieści ', 'pięćdziesiąt ', 'sześćdziesiąt ', 'siedemdziesiąt ', 'osiemdziesiąt ', 'dziewięćdziesiąt ']
setki = ['', 'sto ', 'dwieście ', 'trzysta ', 'czterysta ', 'pięćset ', 'sześćset ', 'siedemset ', 'osiemset ', 'dziewięćset ']


def get_liczebnik_dtct(liczba_float):
    result = {}
    # korekta, sprawdzenie i przygotowanie danych wejściowych (w tym zaokrąglenie do dwóch miejsc po przecinku) 
    liczba_str = '{:0.2f}'.format(liczba_float)
    comma_idx = liczba_str.index('.')
    if comma_idx > 12:
        print('Za duża kwota Max: 999 999 999 999,99 -> BŁĄD #1')
        return None
    cyfry = list(liczba_str)
    # wstawienie spacji co tyrzy cyfry w danych wejściowych
    nowa_liczba_str = liczba_str;
    nowy_comma_idx = nowa_liczba_str.index('.')
    if nowy_comma_idx > 3:
        nowa_liczba_str = insert_str(nowa_liczba_str, ' ', nowy_comma_idx - 3)
    nowy_comma_idx = nowa_liczba_str.index('.')
    if nowy_comma_idx > 7:
        nowa_liczba_str = insert_str(nowa_liczba_str, ' ', nowy_comma_idx - 7)
    nowy_comma_idx = nowa_liczba_str.index('.')
    if nowy_comma_idx > 11:
        nowa_liczba_str = insert_str(nowa_liczba_str, ' ', nowy_comma_idx - 11)
    result['liczba'] = nowa_liczba_str.replace('.', ',')
    # właściwe przetwarzanie liczby na liczebnik
    liczebnik_str = ''
    for i in range(comma_idx - 1, -1, -1):
        if (comma_idx - i) == 1:    # jedności (10^0)
                liczebnik_str = get_trzy_cyfry(cyfry, i) + liczebnik_str
        elif (comma_idx - i) == 2:
            pass
        elif (comma_idx - i) == 3:
            pass
        elif (comma_idx - i) == 4:    # get_tysiące (10^3)
            liczebnik_str = get_trzy_cyfry(cyfry, i) + get_tysiące(cyfry, i) + liczebnik_str
        elif (comma_idx - i) == 5:
            pass
        elif (comma_idx - i) == 6:
            pass
        elif (comma_idx - i) == 7:    # get_get_get_miliardy (10^6)
            liczebnik_str = get_trzy_cyfry(cyfry, i) + get_miliony(cyfry, i) + liczebnik_str
        elif (comma_idx - i) == 8:
            pass
        elif (comma_idx - i) == 9:
            pass
        elif (comma_idx - i) == 10:    # get_miliardy (10^9)
            liczebnik_str = get_trzy_cyfry(cyfry, i) + get_miliardy(cyfry, i) + liczebnik_str
        elif (comma_idx - i) == 11:
            pass
        elif (comma_idx - i) == 12:
            pass
        else:
            print('Za duża kwota Max: 999 999 999 999,99 -> BŁĄD #2')
            return None
    liczebnik_str = liczebnik_str + 'i ' + cyfry[len(cyfry)-2] + cyfry[len(cyfry)-1] + '/100'
    result['liczebnik'] = liczebnik_str
    return result


def get_trzy_cyfry(cyfry_tabl, min_start_tabl_idx):    # przetwarza trzycyfrową liczbę na liczebnik
    liczebnik_str_tym = ''
    if min_start_tabl_idx == 0 or cyfry_tabl[min_start_tabl_idx - 1] != '1':
        if min_start_tabl_idx == 0 or cyfry_tabl[min_start_tabl_idx] != '0':
            liczebnik_str_tym = jedności[int(cyfry_tabl[min_start_tabl_idx])] + liczebnik_str_tym
    if min_start_tabl_idx > 0:
        if cyfry_tabl[min_start_tabl_idx - 1] == '1':
            liczebnik_str_tym = naście[int(cyfry_tabl[min_start_tabl_idx])] + liczebnik_str_tym
        elif cyfry_tabl[min_start_tabl_idx - 1] != '0':
            liczebnik_str_tym = dziesiątki[int(cyfry_tabl[min_start_tabl_idx - 1])] + liczebnik_str_tym
        if min_start_tabl_idx > 1 and cyfry_tabl[min_start_tabl_idx - 2] != '0':
            liczebnik_str_tym = setki[int(cyfry_tabl[min_start_tabl_idx - 2])] + liczebnik_str_tym
    return liczebnik_str_tym


def get_tysiące(cyfry_tabl, min_start_tabl_idx):
    if (min_start_tabl_idx < 2 or cyfry_tabl[min_start_tabl_idx - 2] == '0') and (min_start_tabl_idx < 1 or cyfry_tabl[min_start_tabl_idx - 1] == '0') and cyfry_tabl[min_start_tabl_idx] == '0':
        return ''
    if (min_start_tabl_idx < 2 or cyfry_tabl[min_start_tabl_idx - 2] == '0') and (min_start_tabl_idx < 1 or cyfry_tabl[min_start_tabl_idx - 1] == '0') and cyfry_tabl[min_start_tabl_idx] == '1':
        return 'tysiąc '
    if min_start_tabl_idx > 0 and cyfry_tabl[min_start_tabl_idx - 1] == '1':
        return 'tysięcy '
    if cyfry_tabl[min_start_tabl_idx] == '2' or cyfry_tabl[min_start_tabl_idx] == '3' or cyfry_tabl[min_start_tabl_idx] == '4':
        return 'tysiące '
    else:
        return 'tysięcy '


def get_miliony(cyfry_tabl, min_start_tabl_idx):
    if (min_start_tabl_idx < 2 or cyfry_tabl[min_start_tabl_idx - 2] == '0') and (min_start_tabl_idx < 1 or cyfry_tabl[min_start_tabl_idx - 1] == '0') and cyfry_tabl[min_start_tabl_idx] == '0':
        return ''
    if (min_start_tabl_idx < 2 or cyfry_tabl[min_start_tabl_idx - 2] == '0') and (min_start_tabl_idx < 1 or cyfry_tabl[min_start_tabl_idx - 1] == '0') and cyfry_tabl[min_start_tabl_idx] == '1':
        return 'milion '
    if min_start_tabl_idx > 0 and cyfry_tabl[min_start_tabl_idx - 1] == '1':
        return 'milionów '
    if cyfry_tabl[min_start_tabl_idx] == '2' or cyfry_tabl[min_start_tabl_idx] == '3' or cyfry_tabl[min_start_tabl_idx] == '4':
        return 'miliony '
    else:
        return 'milionów '


def get_miliardy(cyfry_tabl, min_start_tabl_idx):
    if (min_start_tabl_idx < 2 or cyfry_tabl[min_start_tabl_idx - 2] == '0') and (min_start_tabl_idx < 1 or cyfry_tabl[min_start_tabl_idx - 1] == '0') and cyfry_tabl[min_start_tabl_idx] == '0':
        return ''
    if (min_start_tabl_idx < 2 or cyfry_tabl[min_start_tabl_idx - 2] == '0') and (min_start_tabl_idx < 1 or cyfry_tabl[min_start_tabl_idx - 1] == '0') and cyfry_tabl[min_start_tabl_idx] == '1':
        return 'miliard '
    if min_start_tabl_idx > 0 and cyfry_tabl[min_start_tabl_idx - 1] == '1':
        return 'miliardów '
    if cyfry_tabl[min_start_tabl_idx] == '2' or cyfry_tabl[min_start_tabl_idx] == '3' or cyfry_tabl[min_start_tabl_idx] == '4':
        return 'miliardy '
    else:
        return 'miliardów '


def insert_str(source_str, insert_str, pos):
    return source_str[:pos]+insert_str+source_str[pos:]


#============================================================================================================================================
