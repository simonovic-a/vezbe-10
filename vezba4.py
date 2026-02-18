#Napiši funkciju pronadji_reč(ime_fajla, rec) koja vraća koliko puta se reč pojavljuje u
#fajlu.

def pronadji_rec(ime_fajla, rec):
    broj_reci = 0
    with open(ime_fajla, "r") as file:
        for linija in file:
            broj_reci += linija.split().count(rec)
    return broj_reci

print(pronadji_rec("data/data.txt", "test"))