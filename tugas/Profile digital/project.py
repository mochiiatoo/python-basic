nama = input("nama lengkap:")
umur = int(input("umur:")) 
kelas = input("kelas:")
cita_cita = input("cita cita:")
hobi = input("hobi:")
belajar = input("belajar lebih suka malam atau pagi:")
tahun_sekarang = 2025
umur_hitung = tahun_sekarang - umur



tipe = input("ketik '1 wibu' , '2 gamer' , '3 k-popers' , '4 anak konten' , '5 anak nongki': ")
if tipe == "1":
  tipe = "wibu (anak anime banget)"
  tambahan = input("siapa waifumu atau husbando mu? ")
  fav = f"Waifu favorit : {tambahan}"
  komentar = "she is the best waifuu>_<"

elif tipe == "2":
   tipe = "gamer(push rank jalan terus)"
   tambahan = input("game favorit kamu apa?")
   fav = f"game favorit: {tambahan}"
   komentar = "push rank terus glory kaga kwwkkwkwkwkwkkw #_#"

elif tipe == "3":
    tipe = "k-popers(ngikutin gaya korea banget)"
    tambahan = input("bias kamu siapa?")
    fav = f"bias favorit: moch.ridjho syawaludien{tambahan}"
    komentar = "jo-yuri and xinxoo the besttttt"
    
elif tipe == "4":
    tipe = "anak konten(tiktoker/youtuber wanabe)"
    tambahan = input("platform favorit mu apa tiktoker/youtube?")
    fav = f"platform favorit:{tambahan}"
    komentar = "fomo yang ngikutin trend tiktok"

elif tipe == "5":
  tipe = "anak nongki(yang penting ngumpul)"
  tambahan = input("nongkrong lebih sering dimana?")
  fav = f"tempat favorit: {tambahan}"
  komentar = "ngumpul mana aee gassssss!!!!"



print("----- FUN CHECK -----")
print("jawab dengan jujur!!")
jawaban = input("apakah temen di sebelah mu bau?")
if jawaban == "ya":
   komen ="waduh bauu bwangggggg!!!!!>_<"
 
elif jawaban == "tidak":
   komen = "wah wangii mungkin mandi tiap jam wkwkwkwk^_^"




print("===== PROFIL DIGITAL =====")
print(f"nama: {nama}")
print(f"umur: {umur}")
print(f"kelas: {kelas}")
print(f"cita cita:{cita_cita}")
print(f"hobi:{hobi}")
print(f"belajar lebih suka malam atau pagi:{belajar}")
print(f"tahun lahir:{umur_hitung}")

print("===== TIPE DIGITAL ===== ")
print(f"tipe: {tipe}")
print(fav)
print(f"komentar: {komentar}")

print("===== FUN CHECK =====")
print(f"Teman sebelah bau? {jawaban}")
print(f"komen: {komen}")





