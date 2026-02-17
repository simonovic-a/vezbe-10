
#Napiši funkciju upisi_u_fajl(ime_fajla, lista_stringova) koja upisuje sve stringove
#iz liste u fajl, po jedan u red.


messages = [
    "Zdravo svete",
    "Python je super",
    "Učim programiranje",
    "Danas je lep dan"
]

def upisi_u_fajl(file_name, list_of_strings):
    with open(file_name, 'a') as file:
        for string in list_of_strings:
            file.write(string + "\n")

upisi_u_fajl("data/data.txt", messages)