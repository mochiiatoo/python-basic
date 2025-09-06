print("\n----- MATERI 8C - FUNCTION BASIC -----")

#function
# buat fungsi dengan 'def' lalu nama fungsi
# parameter 'nama' untuk mengambil nilai dari luar fungsi
def baca(nama):
    print("komik")
    print("judul:", nama)
baca("leviathan")
baca("good bad fortune")
baca("born from death")

def persegi_panjang(panjang, lebar):
    print("p =", panjang)
    print("L =", lebar)
    rumus = panjang * lebar
    print("hasil luas persegi panjang =", rumus)

persegi_panjang(10, 5)
persegi_panjang(8, 100)


def lingkaran( jari_jari):
    print("J =", jari_jari)
    rumus = 22/5* (jari_jari * jari_jari)
    print("hasil luas lingkaran:", jari_jari)
lingkaran(22)
     


