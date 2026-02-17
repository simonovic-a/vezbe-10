#Napiši funkciju broj_linija(ime_fajla) koja vraća broj linija u fajlu.

def number_of_lines(file_name):
    broj_linija = 0
    with open(file_name, "r") as file:
        for line in file.readlines():
            broj_linija += 1
    return broj_linija

print(number_of_lines("data/data.txt"))