# Multimedia Tugas : 1

def isiform():

    angka1 = int(input("Masukan Angka Pertama : "))
    angka2 = int(input("Masukan Angka Kedua : "))
    return angka1, angka2


def tambah():
    angka1, angka2 = isiform()
    return angka1 + angka2


def kurang():
    angka1, angka2 = isiform()
    return angka1 - angka2


def kali():
    angka1, angka2 = isiform()
    return angka1 * angka2


def bagi():
    angka1, angka2 = isiform()
    return angka1 // angka2


print('/// Operasi Aritmatika ///\n')
print('''
      1. Tambah
      2. Kurang
      3. Kali
      4. Bagi
      ''')

pilihan = int(input('Silahkan Pilih Operasi... '))

operasi = [tambah, kurang, kali, bagi]

hasil = operasi[pilihan-1]()

print('Hasilnya Adalah : ', hasil)
