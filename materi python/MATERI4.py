print("------ MATERI9C LAMBDA ----------")
def areka(nama):
    print(f"areka: {nama}")
    
aya= lambda nama : print(f"aya: {nama}") 

aya("halo ")
areka("halo, siapa ya?")
print("----------------------")
aya("aku aya,kamu murid baru ya?, nama kamu siapa?")
areka("iya aku murid baru, namaku areka")
areka("emm ada apa ya?")
aya("ngga aku mau kenalan ajaa")
areka("emmm okee")
aya("boleh aku dudukk di sini")
areka("iyaa boleh silakan aya")
# high order function (map, sorted, filter )
uang_saku =[100000, 200000, 10000, 20000]
#map[] -> mentraformasi data item
kurangi_jajan = map(lambda uang: uang - 2000, uang_saku)
list_kurangi_jajan = list(kurangi_jajan)
print(f"uang saku: {uang_saku}")
print(f"kuaring jajan: {list_kurangi_jajan}")
# soretd(-> mengurutkan data)
urutkan_uang = sorted(uang_saku)
balik_uang = sorted(uang_saku, reverse=True)
print(f"urutkan uang: {urutkan_uang}")
print(f"urutkan uang terbalik: {balik_uang} ")
#filter( -> menyaring data sesuai kondisi)
filter_uang_gede = filter(lambda uang : uang >50000, uang_saku)
list_uang_gede = list(filter_uang_gede)
print(f"filter uang gede:, {list_uang_gede}")

