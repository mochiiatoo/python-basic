import csv

with open("keuangan.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    data =list(reader)
print(data)

# tampilkan semua data
print("semua data:")
for row in data:
    print (f"{row['Tanggal']} | {row['Keterangan']} | {row['Keterangan']}")

total = sum(int(row["Jumlah"]) for row in data)
print(f"Total pengeruaran: Rp.{total}")