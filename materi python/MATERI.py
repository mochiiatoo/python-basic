print("Materi 6C - python data structures")
print("-----------------------------------")
# List -> [ ] -> berurutan, berubah, boleh duplikat
daftar_belanja = ["pisang kembung", "matcha", "mie ayam", "martabak manis coklat keju^-^"]

print("tas belanja:", daftar_belanja)
print(daftar_belanja[3])
# akses item dengan index
#  append() untuk menambah item akhir list
daftar_belanja.append("siomay")
daftar_belanja.insert(1,"aoka")
daftar_belanja.remove("martabak manis coklat keju^-^")
print("tas belanja sekarang:", daftar_belanja)
# menggabungkan list +
jajanan_assidawi = ["olive chiken", "naspad kawan lamo", "es teh desa"]
jajanan_mochi = ["mochi", "martaabak manis coklat keju", "golda"]
titipan_belanja = jajanan_assidawi = jajanan_mochi
print("titipan belanja:", titipan_belanja)
#menggandakan item list dengan *
print("assidawi;", jajanan_assidawi * 1)

# list bercabang (list multi dimensi)
daftar_menu = [["kopi", "susu", "yoghurt"],#baris 0
               ["jus alpukat", "jus apel", "jus nanas"],# baris 1
               ["es teler", "es cream"]]# baris2

print("daftar menu:", daftar_menu)
print(daftar_menu[2][1])

#tuple -> berurutan, tidak berubah, boleh duplikat
ttl = ("subang", 12, "oktober", 2009)
print("TTL:", ttl)
print("tgl lahir ridho:", ttl[1])
#unpacking variable 9mengestrak tuple ke variable baru selesai urutan
tempat_lahir, tgl_lahir, bln_lahir, thn_lahir = ttl
print("Thn lahir:", thn_lahir)

makanan_list = ["mie ayam", "martabak manis keju cokalt", "siomay"]
print(makanan_list)
for item in makanan_list:
    print(item)


