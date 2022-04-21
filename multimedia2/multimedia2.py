# Awal Function

def kompresi(data):

    hasilKompresi = ""
    hurufSebelumnya = ""
    x = 1
    if not data:
        return ""

    for char in data:
        if char != hurufSebelumnya:
            if hurufSebelumnya:
                hasilKompresi += str(x) + hurufSebelumnya
        x += 1
        hurufSebelumnya = char
    else:
        x = 1
    hasilKompresi += str(x) + hurufSebelumnya
    return hasilKompresi


def dekompresi(data):
    hasilDekompresi = ""
    x = ""
    for char in data:
        if char.isdigit():
            x += char
        else:
            hasilDekompresi += char * int(x)
            x = ""
    return hasilDekompresi

# Akhir Function


# jika ingin mengakses dari file gunakan yang ini
file = open("multimedia2.txt", "r")
kalimat = file.read()


# jika ingin dari inputan user gunakan yang ini
# kalimat = (input("Silakan Ketik Kata/Kalimat : "))

jmlHuruf = len(kalimat)
jmldata = jmlHuruf * 8

print('/// Run Lenght Encode ///\n')
print("Kalimat : ", kalimat)
print("Size = ", jmldata, "Bit")
print("Size = ", jmlHuruf, "Byte")
print("Jumlah Huruf = ", jmlHuruf, "Huruf")
print('''
      Pilih Masukan : 
      
      1. Kompresi
      2. Dekompresi
      ''')

pilihan = (input("Silahkan Masukan Pilihan : "))

# Metode Pertama
if pilihan == "1":
    hasilnya = kompresi(kalimat)
    print("Hasil Kompresi : ", hasilnya)
else:
    hasilnya = dekompresi(kalimat)
    print("Hasil Dekompresi : ", hasilnya)

# Metode Kedua
# if pilihan == "1":
#     hasilnya = kompresi(kalimat)
#     print("Hasil Kompresi : ", hasilnya)
# elif pilihan == "2":
#     hasilnya = dekompresi(kalimat)
#     print("Hasil Dekompresi : ", hasilnya)
# elif pilihan == "3":
#     print("Size = ", jmldata, "Bit")
# elif pilihan == "4":
# print("Jumlah ", jmlHuruf, "Huruf")
# else:
# print("Masukan Salah, Silakan Ulangi")

file.close()
filekompres = open("multimedia2.txt", "w")
filekompres.write(hasilnya)
