import csv

file_path = r"C:\Users\UsEr\Pictures\Saved Pictures\tugas python\tugas\CSV\pesan.txt"
file_pesan = open(file_path, "r")
baca_pesan = file_pesan.read()
print(f"isi pesannya: {baca_pesan}")
file_pesan.close()

("------- Add row csv --------")
file_csv_path = r"C:\SMA IT HSI TUGAS, CIHUYY\materi-file-handling\data.csv"

with open(file_csv_path, "r") as file_alamat:
    baca_alamat = csv.reader(file_alamat)

    list_alamat = list(baca_alamat)
    print(f"daftar alamat: {list_alamat}")
alamat_darian = [9, "darian", "jaktim"]
print(f"alamat baru: {alamat_darian}")
with open(file_csv_path, "a",newline="") as file_alamat:
    tulis_alamat = csv.writer(file_alamat)
    tulis_alamat.writerow(alamat_darian)
    print("selesai")



("-----------------------------------------------------------------------------")
("----- update row csv -------")

file_csv_path = r"C:\SMA IT HSI TUGAS, CIHUYY\materi-file-handling\data.csv"
# buat list kosong untuk menampung data dari csv
data_alamat = []
with open(file_csv_path, "r") as list_alamat:
    baca_alamat = csv.reader(list_alamat)
    for item_alamat in baca_alamat:
        data_alamat.append(item_alamat)

for item in data_alamat:
    if item[1] == 'rain':
        print("data rain di temukan, ganti alamatnya.....")
        item[2] = "bandung" 
    else:
        print("skip data... bukan rain")

del data_alamat[6]
print(f"List data alamat: {data_alamat}")

with open(file_csv_path, "w", newline="") as file_alamat:
    tulis_alamat = csv.writer(file_alamat)
    tulis_alamat.writerows(data_alamat)
    print('--> selesai membuat ulang data csv')