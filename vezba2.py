#Napiši funkciju procitaj_fajl(ime_fajla) koja čita fajl i vraća listu redova.

def read_file(file_name):
    with open(file_name, "r") as file:
        redovi = file.readlines()
        return redovi

print(read_file("data/data.txt"))